function fadeOutAlert(button) {
    console.log(button)
    const alertBox = button.closest('#alert');
    alertBox.classList.add('fade-out');
    setTimeout(() => {
        alertBox.classList.add('hidden');
    }, 500)
}