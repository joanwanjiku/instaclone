
let toggleComments = (id) => {
    console.log('clicked')
    comment = document.getElementById('commentSec')
    if (comment.classList.contains('comments')){
        comment.classList.remove('comments')
    }else {
        comment.classList.add('comments')
    }
}