function abrirModal(videoId) {
    var modal = document.getElementById("videoModal");
    var iframe = document.getElementById("videoIframe");

    // Defina a URL do iframe com o ID do vídeo do Vimeo
    iframe.src = "https://player.vimeo.com/video/" + videoId + "?badge=0&autopause=0&player_id=0&app_id=58479";

    modal.style.display = "block"; // Mostra o modal
}

function fecharModal() {
    var modal = document.getElementById("videoModal");
    var iframe = document.getElementById("videoIframe");

    iframe.src = ""; // Limpa o src do iframe ao fechar o modal
    modal.style.display = "none"; // Oculta o modal
}

// Fecha o modal se o usuário clicar fora dele
window.onclick = function(event) {
    var modal = document.getElementById("videoModal");
    if (event.target == modal) {
        fecharModal();
    }
}
