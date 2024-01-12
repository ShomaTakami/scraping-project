<!-- resources/views/scraping/index.blade.php -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scraping Project</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>Scraping Project</h1>
    <button id="scrapeButton">Scrape Data</button>
    <div id="resultContainer"></div>

    <script>
        $(document).ready(function () {
            $('#scrapeButton').on('click', function () {
                $.get('/scrape-data', function (data) {
                    $('#resultContainer').html('<pre>' + JSON.stringify(data, null, 2) + '</pre>');
                });
            });
        });
    </script>
</body>
</html>
