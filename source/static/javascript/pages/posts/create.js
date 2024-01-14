document.addEventListener('DOMContentLoaded', function () {
    const markdownInput = document.querySelector('#content')
    const markdownPreview = document.querySelector('#markdown-preview')

    markdownInput.addEventListener('input', () => {
        markdownPreview.innerHTML = marked.parse(markdownInput.value)
    })
})

document.addEventListener('DOMContentLoaded', function () {
    const titleInput = document.querySelector('#title')
    const titlePreview = document.querySelector('#title-preview')

    titleInput.addEventListener('input', () => {
        titlePreview.innerHTML = titleInput.value
    })
})