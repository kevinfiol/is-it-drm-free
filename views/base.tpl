<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/static/bamboo.min.css">
    <link rel="stylesheet" type="text/css" href="/static/main.css">
    <title>Is It DRM-Free?</title>
</head>
<body>
    <main>
        <h1><a href="/">Is It DRM-Free?</a></h1>
        <form action="/results" method="POST" id="game-form">
            <noscript>
                <input type="text" name="game_name" value="{{ game_name }}" placeholder="Search for DRM-Free games">
            </noscript>

            <div id="etto-container" input-value="{{ game_name }}"></div>
            <div class="flex flex-column my1">
                <button type="submit" class="align-end">Search</button>
            </div>
        </form>
        {{!base}}
    </main>
    <script type="text/javascript" src="/static/etto.min.js"></script>
    <script type="text/javascript" src="/static/app.js"></script>
</body>
</html>