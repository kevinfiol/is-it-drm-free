% rebase('base.tpl', game_name=game_name)

%if not game_exists:
    <div class="result-subtitle">
        <h2>{{ game_name.upper() }} not found.</h2>
        <p>Try searching again?</p>
    </div>
%else:
    %isDrmFree = len(prices) > 0

    %if isDrmFree:
        <h2 class="result-answer">Yes.</h2>
    %else:
        <h2 class="result-answer">No.</h2>
    %end

    <div class="result-subtitle">
        <h2>{{ game_name.upper() + (' is available DRM-Free.' if isDrmFree else ' is NOT available DRM-Free.') }}</h2>
        <a href="https://isthereanydeal.com/game/{{ plain_id }}">More info at IsThereAnyDeal.com</a>
    </div>

    %if len(prices) > 0:
        % for price in prices:
            <article class="result-price">
                <header>
                    <a href="{{ price['url'] }}">{{ price['shop']['name'] }} ${{ price['price_new'] }}</a>
                </header>
                <span>
                    % for idx, drm in enumerate(price['drm']):
                        {{ drm + (', ' if idx != len(price['drm']) - 1 else '') }}
                    % end
                </span>
            </article>
        % end
    %end

    <div class="disclaimers">
        <small>
            Note: <a href="https://isthereanydeal.com">IsThereAnyDeal.com</a> does not provide DRM information for <a href="https://itch.io">itch.io</a>. While titles available on itch.io are typically DRM-Free, some developers choose to instead distribute their titles as license keys to other storefronts with DRM (Such as Steam). Please confirm that a title is DRM-Free before purchasing from itch.io.
        </small>
    </div>
%end

<p>
    <a target="_blank" href="https://isthereanydeal.com/search/?q={{ game_name }}">Search on IsThereAnyDeal.com</a>
</p>