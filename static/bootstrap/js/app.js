particlesJS("particles-js", {
    particles: {
      number: {
        value: 80, // Número de partículas
        density: {
          enable: true,
          value_area: 800 // Área onde as partículas serão exibidas
        }
      },
      color: {
        value: "#ffffff" // Cor das partículas
      },
      shape: {
        type: "circle", // Formato das partículas (círculo, quadrado, etc.)
        stroke: {
          width: 0,
          color: "#000000"
        }
      },
      opacity: {
        value: 0.5, // Opacidade das partículas
        random: false,
        anim: {
          enable: false
        }
      },
      size: {
        value: 4, // Tamanho das partículas
        random: true,
        anim: {
          enable: false
        }
      },
      line_linked: {
        enable: false
      },
      move: {
        enable: true,
        speed: 3, // Velocidade de movimento das partículas
        direction: "none",
        random: false,
        straight: false,
        out_mode: "out",
        bounce: false,
        attract: {
          enable: false,
          rotateX: 600,
          rotateY: 1200
        }
      }
    },
    interactivity: {
      detect_on: "canvas",
      events: {
        onhover: {
          enable: false
        },
        onclick: {
          enable: false
        },
        resize: true
      }
    },
    retina_detect: true
  });