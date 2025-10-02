var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(event) {
        var post = event.target.closest('.one-post'); // Находим родителя с классом one-post
        if (post.classList.contains('folded')) {
            post.classList.remove('folded');
            event.target.innerHTML = "Свернуть";
        } else {
            post.classList.add('folded');
            event.target.innerHTML = "Развернуть";
        }
    });
}
