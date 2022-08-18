const scales = ["year", "month", "day"];
const scale = scales[0];

function displayPosts(data) {
    var container = document.getElementById("posts");
    data.posts.forEach(post => {
        var p = document.createElement("span");
        p.className = "post";

        var title = document.createElement("h3");
        title.textContent = "- " + post.title;
        p.appendChild(title);

        var author = document.createElement("p");
        var bold = document.createElement("b");
        bold.textContent = "Author: " + post.author;
        author.appendChild(bold);
        p.appendChild(author);

        var time = document.createElement("p");
        time.textContent = scale + " " + post.formatted_date;
        p.appendChild(time);

        var content = document.createElement("p");
        content.innerHTML = post.content;
        p.appendChild(content);

        container.appendChild(p);
        container.appendChild(document.createElement("br"));
    });
}

window.onload = (event) => {
    fetch("/posts-on?scale="+scale)
        .then((response) => response.json())
        .then((data) => displayPosts(data))
}