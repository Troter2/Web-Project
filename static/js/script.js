$(document).ready(function() {
    // Obtener el contenedor de películas
    var moviesContainer = $('#movies-container');

    // Iterar sobre cada película y mostrarla en la página
    $.each(data, function(index, movie) {
        // Crear un nuevo elemento para la película
        var movieElement = $('<div class="movie"></div>');

        // Agregar el título de la película
        var title = $('<h2>' + movie.title + '</h2>');
        movieElement.append(title);

        // Agregar la imagen de la película
        var poster = $('<img src="https://image.tmdb.org/t/p/w500' + movie.poster_path + '" alt="' + movie.title + '">');
        movieElement.append(poster);

        // Agregar la descripción de la película
        var overview = $('<p>' + movie.overview + '</p>');
        movieElement.append(overview);

        // Agregar el elemento de la película al contenedor
        moviesContainer.append(movieElement);
    });
});
