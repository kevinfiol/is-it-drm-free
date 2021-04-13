(function(Etto) {
    'use strict';

    const gameForm = document.getElementById('game-form');
    if (gameForm) mountEtto();

    function mountEtto() {
        const ettoContainer = document.getElementById('etto-container');
        const defaultValue = ettoContainer.getAttribute('input-value');

        const etto = new Etto(ettoContainer, {
            inputAttributes: { name: 'game_name', placeholder: 'Search for DRM-Free games' },
            requestDelay: 250,
            source: searchSource,
            maxResults: 15,
            filterFn: (inputVal, choices) => choices,
            onSelect
        });

        etto.value = defaultValue;

        function onSelect(choice) {
            const hiddenInput = document.createElement('input');
            hiddenInput.setAttribute('hidden', 'true');
            hiddenInput.setAttribute('name', 'plain_id');
            hiddenInput.setAttribute('value', choice.plain_id);
            gameForm.appendChild(hiddenInput);
            gameForm.submit();
        }

        let controller;
        async function searchSource(query, done) {
            if (controller) controller.abort();
            controller = new AbortController();

            try {
                const choices = [];
                const response = await fetch(`/search/${query}`, {
                    signal: controller.signal
                });

                controller = null;
                const json = await response.json();

                if (json.data && json.data.results) {
                    json.data.results.forEach(game => {
                        const gameTitle = game.title.replace(/[^\x00-\x7F]/g, '');
                        choices.push({
                            label: gameTitle,
                            value: gameTitle,
                            plain_id: game.plain
                        })
                    });
                }

                done(choices);
            } catch(err) {
                if (err.name !== 'AbortError') {
                    done([]);
                    throw err;
                }
            }
        }
    }
})(Etto);