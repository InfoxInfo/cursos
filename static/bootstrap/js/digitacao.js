// Função para atualizar o texto do botão quando a tecla Caps Lock é pressionada
function atualizarTextoBotao() {
    var capsLockAtivo = event.getModifierState && event.getModifierState('CapsLock');
    var shiftAtivo = event.getModifierState && event.getModifierState('Shift');
    
    // Verifica se o Caps Lock está ativo
    if (capsLockAtivo || shiftAtivo) {
    document.getElementById('b_q').innerHTML = 'Q';
    document.getElementById('b_w').innerHTML = 'W';
    document.getElementById('b_e').innerHTML = 'E';
    document.getElementById('b_r').innerHTML = 'R';
    document.getElementById('b_t').innerHTML = 'T';
    document.getElementById('b_y').innerHTML = 'Y';
    document.getElementById('b_u').innerHTML = 'U';
    document.getElementById('b_i').innerHTML = 'I';
    document.getElementById('b_o').innerHTML = 'O';
    document.getElementById('b_p').innerHTML = 'P';

    document.getElementById('b_a').innerHTML = 'A';
    document.getElementById('b_s').innerHTML = 'S';
    document.getElementById('b_d').innerHTML = 'D';
    document.getElementById('b_f').innerHTML = 'F';
    document.getElementById('b_g').innerHTML = 'G';
    document.getElementById('b_h').innerHTML = 'H';
    document.getElementById('b_j').innerHTML = 'J';
    document.getElementById('b_k').innerHTML = 'K';
    document.getElementById('b_l').innerHTML = 'L';
    document.getElementById('b_ç').innerHTML = 'Ç';

    document.getElementById('b_z').innerHTML = 'Z';
    document.getElementById('b_x').innerHTML = 'X';
    document.getElementById('b_c').innerHTML = 'C';
    document.getElementById('b_v').innerHTML = 'V';
    document.getElementById('b_x').innerHTML = 'X';
    document.getElementById('b_b').innerHTML = 'B';
    document.getElementById('b_n').innerHTML = 'N';
    document.getElementById('b_m').innerHTML = 'M';
    } else {
    document.getElementById('b_q').innerHTML = 'q';
    document.getElementById('b_w').innerHTML = 'w';
    document.getElementById('b_e').innerHTML = 'e';
    document.getElementById('b_r').innerHTML = 'r';
    document.getElementById('b_t').innerHTML = 't';
    document.getElementById('b_y').innerHTML = 'y';
    document.getElementById('b_u').innerHTML = 'u';
    document.getElementById('b_i').innerHTML = 'i';
    document.getElementById('b_o').innerHTML = 'o';
    document.getElementById('b_p').innerHTML = 'p';

    document.getElementById('b_a').innerHTML = 'a';
    document.getElementById('b_s').innerHTML = 's';
    document.getElementById('b_d').innerHTML = 'd';
    document.getElementById('b_f').innerHTML = 'f';
    document.getElementById('b_g').innerHTML = 'g';
    document.getElementById('b_h').innerHTML = 'h';
    document.getElementById('b_j').innerHTML = 'j';
    document.getElementById('b_k').innerHTML = 'k';
    document.getElementById('b_l').innerHTML = 'l';
    document.getElementById('b_ç').innerHTML = 'ç';

    document.getElementById('b_z').innerHTML = 'z';
    document.getElementById('b_x').innerHTML = 'x';
    document.getElementById('b_c').innerHTML = 'c';
    document.getElementById('b_v').innerHTML = 'v';
    document.getElementById('b_x').innerHTML = 'x';
    document.getElementById('b_b').innerHTML = 'b';
    document.getElementById('b_n').innerHTML = 'n';
    document.getElementById('b_m').innerHTML = 'm';
    }
    if (shiftAtivo) {
    document.getElementById('b_barra').innerHTML = '|';
    document.getElementById('b_doispontos').innerHTML = ':';
    document.getElementById('b_interrogacao').innerHTML = '?';
    document.getElementById('b_maior').innerHTML = '>';
    document.getElementById('b_menor').innerHTML = '<';
    document.getElementById('b_til').innerHTML = '^';
    document.getElementById('b_fechacol').innerHTML = '}';
    document.getElementById('b_abrecol').innerHTML = '{';
    document.getElementById('b_agudo').innerHTML = '`';
    document.getElementById('b_igual').innerHTML = '+';
    document.getElementById('b_under').innerHTML = '_';
    document.getElementById('b_zeroa').innerHTML = ')';
    document.getElementById('b_nove').innerHTML = '(';
    document.getElementById('b_oito').innerHTML = '*';
    document.getElementById('b_sete').innerHTML = '&';
    document.getElementById('b_seis').innerHTML = '¨';
    document.getElementById('b_cinco').innerHTML = '%';
    document.getElementById('b_quatro').innerHTML = '$';
    document.getElementById('b_tres').innerHTML = '#';
    document.getElementById('b_dois').innerHTML = '@';
    document.getElementById('b_um').innerHTML = '!';
    document.getElementById('b_aspas').innerHTML = '"';
    } else {
    document.getElementById('b_barra').innerHTML = '\\';
    document.getElementById('b_doispontos').innerHTML = ';';
    document.getElementById('b_interrogacao').innerHTML = '/';
    document.getElementById('b_maior').innerHTML = '.';
    document.getElementById('b_menor').innerHTML = ',';

    document.getElementById('b_til').innerHTML = '~';
    document.getElementById('b_fechacol').innerHTML = ']';
    document.getElementById('b_abrecol').innerHTML = '[';
    document.getElementById('b_agudo').innerHTML = '´';
    document.getElementById('b_igual').innerHTML = '=';
    document.getElementById('b_under').innerHTML = '-';
    document.getElementById('b_zeroa').innerHTML = '0';
    document.getElementById('b_nove').innerHTML = '9';
    document.getElementById('b_oito').innerHTML = '8';
    document.getElementById('b_sete').innerHTML = '7';
    document.getElementById('b_seis').innerHTML = '6';
    document.getElementById('b_cinco').innerHTML = '5';
    document.getElementById('b_quatro').innerHTML = '4';
    document.getElementById('b_tres').innerHTML = '3';
    document.getElementById('b_dois').innerHTML = '2';
    document.getElementById('b_um').innerHTML = '1';
    document.getElementById('b_aspas').innerHTML = "'";
    }
}

// Chama a função de atualização quando uma tecla é pressionada
document.onkeydown = atualizarTextoBotao;
document.onkeyup = atualizarTextoBotao;

// Função para adicionar a classe 'active' ao botão quando uma tecla é pressionada
function changeButtonColor(event) {
    var fixa = document.getElementById('fixa');
    var enter = document.getElementById('enter');
    var backspace = document.getElementById('backspace');
    var shiftLeft = document.getElementById('shiftLeft');
    var shiftRight = document.getElementById('shiftRight');
    var space = document.getElementById('space');
    var b_a = document.getElementById('b_a');
    var b_s = document.getElementById('b_s');
    var b_d = document.getElementById('b_d');
    var b_f = document.getElementById('b_f');
    var b_g = document.getElementById('b_g');
    var b_h = document.getElementById('b_h');
    var b_j = document.getElementById('b_j');
    var b_k = document.getElementById('b_k');
    var b_l = document.getElementById('b_l');
    var b_ç = document.getElementById('b_ç');
    var b_til = document.getElementById('b_til');
    var b_fechacol = document.getElementById('b_fechacol');
    

    var b_q = document.getElementById('b_q');
    var b_w = document.getElementById('b_w');
    var b_e = document.getElementById('b_e');
    var b_r = document.getElementById('b_r');
    var b_t = document.getElementById('b_t');
    var b_y = document.getElementById('b_y');
    var b_u = document.getElementById('b_u');
    var b_i = document.getElementById('b_i');
    var b_o = document.getElementById('b_o');
    var b_p = document.getElementById('b_p');
    var b_agudo = document.getElementById('b_agudo');
    var b_abrecol = document.getElementById('b_abrecol');

    var b_barra = document.getElementById('b_barra');
    var b_z = document.getElementById('b_z');
    var b_x = document.getElementById('b_x');
    var b_c = document.getElementById('b_c');
    var b_v = document.getElementById('b_v');
    var b_b = document.getElementById('b_b');
    var b_n = document.getElementById('b_n');
    var b_m = document.getElementById('b_m');
    var b_menor = document.getElementById('b_menor');
    var b_maior = document.getElementById('b_maior');
    var b_doispontos = document.getElementById('b_doispontos');
    var b_interrogacao = document.getElementById('b_interrogacao');
    
    var b_aspas = document.getElementById('b_aspas');
    var b_um = document.getElementById('b_um');
    var b_dois = document.getElementById('b_dois');
    var b_tres = document.getElementById('b_tres');
    var b_quatro = document.getElementById('b_quatro');
    var b_cinco = document.getElementById('b_cinco');
    var b_seis = document.getElementById('b_seis');
    var b_sete = document.getElementById('b_sete');
    var b_oito = document.getElementById('b_oito');
    var b_nove = document.getElementById('b_nove');
    var b_zeroa = document.getElementById('b_zeroa');
    var b_under = document.getElementById('b_under');
    var b_igual = document.getElementById('b_igual');
    
    
  if (event.getModifierState('CapsLock')) {
    fixa.classList.add('active');
  } else {
      fixa.classList.remove('active');
  }

  if (event.key === 'Enter') {
    enter.classList.add('active');
  }
  if (event.key === 'Backspace') {
    backspace.classList.add('active');
  }

  if (event.getModifierState('Shift')) {
    if (event.location === 1) {
      shiftLeft.classList.add('active');
    } else if (event.location === 2) {
      shiftRight.classList.add('active');
    }
  }
  if (event.key === ' ') {
    space.classList.add('active');
  }
    var key = event.key.toLowerCase();

    if (key === 'a') {
      b_a.classList.add('active');
    }
    if (key === 's') {
      b_s.classList.add('active');
    }
    if (key === 'd') {
      b_d.classList.add('active')
    }
    if (key === 'f') {
      b_f.classList.add('active')
    }
    if (key === 'g') {
      b_g.classList.add('active')
    }
    if (key === 'h') {
      b_h.classList.add('active')
    }
    if (key === 'j') {
      b_j.classList.add('active')
    }
    if (key === 'k') {
      b_k.classList.add('active')
    }
    if (key === 'l') {
      b_l.classList.add('active')
    }
    if (key === 'ç') {
      b_ç.classList.add('active')
    }
    if (key === 'q') {
      b_q.classList.add('active')
    }
    if (key === 'w') {
      b_w.classList.add('active')
    }
    if (key === 'e') {
      b_e.classList.add('active')
    }
    if (key === 'r') {
      b_r.classList.add('active')
    }
    if (key === 't') {
      b_t.classList.add('active')
    }
    if (key === 'y') {
      b_y.classList.add('active')
    }
    if (key === 'u') {
      b_u.classList.add('active')
    }
    if (key === 'i') {
      b_i.classList.add('active')
    }
    if (key === 'o') {
      b_o.classList.add('active')
    }
    if (key === 'p') {
      b_p.classList.add('active')
    }
    if (key === 'z') {
      b_z.classList.add('active');
    }
    if (key === 'x') {
      b_x.classList.add('active');
    }
    if (key === 'c') {
      b_c.classList.add('active');
    }
    if (key === 'v') {
      b_v.classList.add('active');
    }
    if (key === 'b') {
      b_b.classList.add('active');
    }
    if (key === 'n') {
      b_n.classList.add('active');
    }
    if (key === 'm') {
      b_m.classList.add('active');
    }
    if (key === '\\' || key === '|') {
      b_barra.classList.add('active');
    }
    if (key === ',' || key === '<') {
      b_menor.classList.add('active');
    }
    if (key === '.' || key === '>') {
      b_maior.classList.add('active');
    }
    if (key === ';' || key === ':') {
      b_doispontos.classList.add('active');
    }
    if (key === '/' || key === '?') {
      b_interrogacao.classList.add('active');
    }
    if (key === '~' || key === '^') {
      b_til.classList.add('active');
    }
    if (key === ']' || key === '}') {
      b_fechacol.classList.add('active');
    }
    if (key === "´" || key === "`") {
      b_agudo.classList.add('active');
    }
    if (key === '[' || key === '{') {
      b_abrecol.classList.add('active');
    }
    if (key === "'" || key === '"') {
      b_aspas.classList.add('active');
    }
    if (event.key === '1' || key === '!') {
      b_um.classList.add('active');
    }
    if (key === "2" || key === '@') {
      b_dois.classList.add('active');
    }
    if (key === "3" || key === '#') {
        b_tres.classList.add('active');
    }
    if (key === "4" || key === '$') {
        b_quatro.classList.add('active');
    }
    if (key === "5" || key === '%') {
        b_cinco.classList.add('active');
    }
    if (key === '6' || key === '¨') {
        b_seis.classList.add('active');
      }
    if (key === "7" || key === '&') {
        b_sete.classList.add('active');
    }
    if (key === "8" || key === '*') {
        b_oito.classList.add('active');
    }
    if (key === "9" || key === '(') {
        b_nove.classList.add('active');
    }
    if (key === '0' || key === ')') {
        b_zeroa.classList.add('active');
    }
    if (key === '-' || key === '_') {
        b_under.classList.add('active');
    }
    if (key === '=' || key === '+') {
        b_igual.classList.add('active');
    }
    
  }

  // Função para remover a classe 'active' do botão quando a tecla é liberada
  function resetButtonColor(event) {
    var enter = document.getElementById('enter');
    var backspace = document.getElementById('backspace');
    var shiftLeft = document.getElementById('shiftLeft');
    var shiftRight = document.getElementById('shiftRight');
    var shiftRight = document.getElementById('shiftRight');
    var space = document.getElementById('space');
    var b_a = document.getElementById('b_a');
    var b_s = document.getElementById('b_s');
    var b_d = document.getElementById('b_d');
    var b_f = document.getElementById('b_f');
    var b_g = document.getElementById('b_g');
    var b_h = document.getElementById('b_h');
    var b_j = document.getElementById('b_j');
    var b_k = document.getElementById('b_k');
    var b_l = document.getElementById('b_l');
    var b_ç = document.getElementById('b_ç');
    var b_til = document.getElementById('b_til');
    var b_fechacol = document.getElementById('b_fechacol');


    var b_q = document.getElementById('b_q');
    var b_w = document.getElementById('b_w');
    var b_e = document.getElementById('b_e');
    var b_r = document.getElementById('b_r');
    var b_t = document.getElementById('b_t');
    var b_y = document.getElementById('b_y');
    var b_u = document.getElementById('b_u');
    var b_i = document.getElementById('b_i');
    var b_o = document.getElementById('b_o');
    var b_p = document.getElementById('b_p');
    var b_agudo = document.getElementById('b_agudo');
    var b_abrecol = document.getElementById('b_abrecol');

    var b_barra = document.getElementById('b_barra');
    var b_z = document.getElementById('b_z');
    var b_x = document.getElementById('b_x');
    var b_c = document.getElementById('b_c');
    var b_v = document.getElementById('b_v');
    var b_b = document.getElementById('b_b');
    var b_n = document.getElementById('b_n');
    var b_m = document.getElementById('b_m');
    var b_menor = document.getElementById('b_menor');
    var b_maior = document.getElementById('b_maior');
    var b_doispontos = document.getElementById('b_doispontos');
    var b_interrogacao = document.getElementById('b_interrogacao');

    var b_aspas = document.getElementById('b_aspas');
    var b_um = document.getElementById('b_um');
    var b_dois = document.getElementById('b_dois');
    var b_tres = document.getElementById('b_tres');
    var b_quatro = document.getElementById('b_quatro');
    var b_cinco = document.getElementById('b_cinco');
    var b_seis = document.getElementById('b_seis');
    var b_sete = document.getElementById('b_sete');
    var b_oito = document.getElementById('b_oito');
    var b_nove = document.getElementById('b_nove');
    var b_zeroa = document.getElementById('b_zeroa');
    var b_under = document.getElementById('b_under');
    var b_igual = document.getElementById('b_igual');

    var key = event.key.toLowerCase();

    if (key === 'shift') {
      if (event.location === 1) {
          shiftLeft.classList.remove('active');
        } else if (event.location === 2) {
          shiftRight.classList.remove('active');
        }
    }

    if (key === 'enter') {
      enter.classList.remove('active');
    }
    if (event.key === ' ') {
      space.classList.remove('active');
    }
    
    if (key === 'backspace') {
      backspace.classList.remove('active');
    }
    if (event.key === 'shift') {
      shift.classList.remove('active');
  }
    if (key === 'a') {
      b_a.classList.remove('active');
    }
    if (key === 's') {
      b_s.classList.remove('active');
    }
    if (key === 'd') {
      b_d.classList.remove('active');
    }
    if (key === 'f') {
      b_f.classList.remove('active');
    }
    if (key === 'g') {
      b_g.classList.remove('active');
    }
    if (key === 'h') {
      b_h.classList.remove('active');
    }
    if (key === 'j') {
      b_j.classList.remove('active');
    }
    if (key === 'k') {
      b_k.classList.remove('active');
    }
    if (key === 'l') {
      b_l.classList.remove('active');
    }
    if (key === 'ç') {
      b_ç.classList.remove('active');
    }
    if (key === 'q') {
      b_q.classList.remove('active');
    }
    if (key === 'w') {
      b_w.classList.remove('active');
    }
    if (key === 'e') {
      b_e.classList.remove('active');
    }
    if (key === 'r') {
      b_r.classList.remove('active');
    }
    if (key === 't') {
      b_t.classList.remove('active');
    }
    if (key === 'y') {
      b_y.classList.remove('active');
    }
    if (key === 'u') {
      b_u.classList.remove('active');
    }
    if (key === 'i') {
      b_i.classList.remove('active');
    }
    if (key === 'o') {
      b_o.classList.remove('active');
    }
    if (key === 'p') {
      b_p.classList.remove('active');
    }
    if (key === 'z') {
      b_z.classList.remove('active');
    }
    if (key === 'x') {
      b_x.classList.remove('active');
    }
    if (key === 'c') {
      b_c.classList.remove('active');
    }
    if (key === 'v') {
      b_v.classList.remove('active');
    }
    if (key === 'b') {
      b_b.classList.remove('active');
    }
    if (key === 'n') {
      b_n.classList.remove('active');
    }
    if (key === 'm') {
      b_m.classList.remove('active');
    }
    if (key === '\\' || key === '|') {
      b_barra.classList.remove('active');
    }

    if (key === ',' || key === '<') {
      b_menor.classList.remove('active');
    }
    if (key === '.' || key === '>') {
      b_maior.classList.remove('active');
    }
    if (key === ';' || key === ':') {
      b_doispontos.classList.remove('active');
    }
    if (key === '/' || key === '?') {
      b_interrogacao.classList.remove('active');
    }
    if (key === '~' || key === '^') {
      b_til.classList.remove('active');
    }
    if (key === ']' || key === '}') {
      b_fechacol.classList.remove('active');
    }
    if (key === "´" || key === "`") {
      b_agudo.classList.remove('active');
    }
    if (key === '[' || key === '{') {
      b_abrecol.classList.remove('active');
    }
    if (key === "'" || key === '"') {
      b_aspas.classList.remove('active');
    }
    if (event.key === '1' || key === '!') {
      b_um.classList.remove('active');
    }
    if (event.key === '2' || key === '@') {
      b_dois.classList.remove('active');
    }
    if (event.key === '3' || key === '#') {
        b_tres.classList.remove('active');
    }
    if (event.key === '4' || key === '$') {
        b_quatro.classList.remove('active');
    }
    if (event.key === '5' || key === '%') {
        b_cinco.classList.remove('active');
    }
    if (key === '6' || key === '¨') {
        b_seis.classList.remove('active');
      }
    if (event.key === '7' || key === '&') {
        b_sete.classList.remove('active');
    }
    if (event.key === '8' || key === '*') {
        b_oito.classList.remove('active');
    }
    if (event.key === '9' || key === '(') {
        b_nove.classList.remove('active');
    }
    if (key === '0' || key === ')') {
        b_zeroa.classList.remove('active');
    }
    if (key === '-' || key === '_') {
        b_under.classList.remove('active');
    }
    if (key === '=' || key === '+') {
        b_igual.classList.remove('active');
    }
    
  }

  // Adiciona os event listeners aos eventos de pressionar e liberar teclas
  document.addEventListener('keydown', changeButtonColor);
  document.addEventListener('keyup', resetButtonColor);

  $(document).ready(function() {
    var currentIndex = 0;
    var counter = 0; // Variável para armazenar o contador
    var cont = 0;
    var erroPrimeiro = 0;
    var contLicoes = 0; // Variável para armazenar o número de lições
    
    $('.typed-input').on('input', function() {
      var typedText = $(this).val();
      var currentLetter = $('.letter').eq(currentIndex).text();

      if (typedText.charAt(typedText.length - 1) !== currentLetter) {
        $(this).val(typedText.slice(0, -1));
        if(erroPrimeiro === 0){
          cont++;
          erroPrimeiro++;
        }
      } else {
        erroPrimeiro = 0;
        currentIndex++;
        $('.letter').eq(currentIndex - 1).addClass('typed');

        if (currentIndex === $('.letter').length) { // Verifica se chegou ao final da frase
          counter++; // Incrementa o contador
          $(this).val(''); // Limpa o campo de entrada
          currentIndex = 0; // Reinicia o índice
          $('.letter').removeClass('typed'); // Remove a classe 'typed' das letras
          updateCounters(); // Atualiza os contadores correspondentes
        }
      }
      $('button[data-repeticao]').each(function() {
        var numeroLetras = $('.letter').length; // Obtém o número de elementos com a classe .letter
        var repeticao = $(this).data('repeticao');
        $('#numero-letras-btn').text((100 - (cont * 100 / (repeticao * numeroLetras))).toFixed(2) + " %"); // Define o valor do atributo data-repeticao no elemento desejado
        
      });

      $('#contagem').text(cont); // Exibe o valor de 'cont' em um elemento com id 'contagem'
  });

// Função para registrar os dados da lição
function registrarDadosLicao() {
  var licao_atual = $('#licao_agora').text();
  var toques = $('#toques-por-minuto-btn').text();
  var tempo = $('#tempo').text();
  var tempo = parseFloat(tempo.replace(':', '.'));
  var acertos = $('#numero-letras-btn').text();
  var acertos = parseFloat(acertos.replace(',', '.'));
  var erros = $('#contagem').text();
  

  var data = {
    'licao_atual': licao_atual,
    'toques': toques,
    'acertos': acertos,
    'erros': erros,
    'tempo': tempo
  };

  $.ajax({
    url: '/cursodigitacao/relatorioDigitacao/',
    type: 'POST',
    data: data,
    success: function(response) {
      // Lógica de manipulação de sucesso aqui
      
      // Atualizar o valor de 'acertos' com o valor retornado do servidor (se necessário)
      acertos = response.acertos;
    },
    error: function(xhr, textStatus, errorThrown) {
      // Lógica de manipulação de erro aqui
    }
  });
}
  
  // Evento de clique no botão "my-button"
  $('#my-button').on('click', function() {
    
    // Registra os dados da lição
    registrarDadosLicao();

});


  // Evento de clique no botão "proximoBotao"
  const proximoBotao = document.getElementById('proximo-botao');
  const inscricaoId = '{{ inscricoes.first.id }}';

  proximoBotao.addEventListener('click', function(event) {
    event.preventDefault();
    window.location.href = "{% url 'cursodigitacao_next' 0 %}".replace('0', inscricaoId);
    contLicoes = contLicoes + 1;
    $('#contLicoes').text(contLicoes);
  });



    // Desativa o Backspace
    $('.typed-input').on('keydown', function(e) {
      if (e.keyCode === 8) {
        e.preventDefault();
      }
    });

    $('.typed-input').focus();
    $(document).ready(function() {
        $('div').click(function() {
          $('.typed-input').focus();
        });
      });

  function updateCounters() {
  var counters = $('.counter'); // Encontra todos os elementos de contador
    counters.each(function() {
      var currentCounter = $(this);
      var currentValue = parseInt(currentCounter.text());
      currentCounter.text(currentValue + 1); // Incrementa o contador

      var digRepeticao = currentCounter.parent().data('repeticao');
      console.log("O valor de dig.repeticao é: " + digRepeticao);

      var proximoBotao = $('#proximo-botao');
      var inputElement = $('#input-element');
      var btnreiniciar = $('#btn-reiniciar');

      if (currentValue === digRepeticao) {
        clearInterval(timerInterval); // Pausa o timer
        proximoBotao.show();
        inputElement.hide();
        btnreiniciar.hide();
      } else {
        proximoBotao.hide();
        inputElement.show();
        btnreiniciar.show();
      }
    });
}

    updateCounters(); // Atualiza os contadores inicialmente


    var startTime; // Variável para armazenar o tempo de início
    var timerInterval; // Variável para armazenar o intervalo do timer

    $('.typed-input').on('input', function() {
      if (!startTime) {
        startTime = new Date(); // Define o tempo de início se ainda não estiver definido
        startTimer(); // Inicia o timer
      }
    });


    function startTimer() {
      timerInterval = setInterval(updateTimer, 1000); // Atualiza o timer a cada segundo
    }

    function updateTimer() {
      var currentTime = new Date();
      var elapsedTime = currentTime - startTime;
      var seconds = Math.floor(elapsedTime / 1000);
      $('#tempo').text(formatTime(seconds));
    }


    function formatTime(seconds) {
      var minutes = Math.floor(seconds / 60);
      var remainingSeconds = seconds % 60;

      // Formata os minutos e segundos como "00:00"
      var formattedMinutes = String(minutes).padStart(2, '0');
      var formattedSeconds = String(remainingSeconds).padStart(2, '0');

      return formattedMinutes + ':' + formattedSeconds;
    }


    // Evento de clique no botão "Reiniciar"
    $('#btn-reiniciar').on('click', function() {
      clearInterval(timerInterval); // Para o timer
      startTime = 0; // Reseta o tempo de início para 0
      $('#tempo').text('00:00'); // Zera a contagem exibida
      counter = 0; // Reseta o contador para zero
      $('.typed-input').val(''); // Limpa o campo de entrada
      $('.counter').text('1'); // Reinicia os contadores para zero
      $('.letter').removeClass('typed'); // Remove a classe 'typed' das letras
      currentIndex = 0; // Reinicia o índice para zero
      $('.typed-input').focus(); // Define o foco no input
      toques = 0; // Reinicia a contagem de toques por minuto
      $('#toques-por-minuto-btn').text('0');
      tempoInicial = 0;
      $('#numero-letras-btn').text('0'); // Reinicia os 
      $('#contagem').text('0'); // Reinicia os 

    });


// Captura o elemento de input e o botão
const input = document.querySelector('.typed-input');
const button = document.querySelector('#toques-por-minuto-btn');

// Variável para armazenar a quantidade de toques
let toques = 0;
let tempoInicial = 0; // Inicialmente definido como zero

// Incrementa a quantidade de toques quando o input receber um evento de digitação
input.addEventListener('input', function() {
  toques++;

  if (tempoInicial === 0) {
    tempoInicial = new Date().getTime(); // Inicia a contagem de tempo
  }

  const tempoAtual = new Date().getTime();
  const diferencaTempo = tempoAtual - tempoInicial;
  const minutos = diferencaTempo / 1000 / 60;

  let toquesPorMinuto;
  if (minutos !== 0) {
    toquesPorMinuto = toques / minutos;
  } else {
    toquesPorMinuto = 0;
  }
  toquesPorMinuto = Math.round(toquesPorMinuto);

  button.innerText = toquesPorMinuto.toString();

  var digRepeticao = button.dataset.repeticao; // Atribui o valor de data-repeticao ao botão
  var currentValue = parseInt($('.counter').text());

  if (currentValue === parseInt(digRepeticao)) {
    clearInterval(timerInterval); // Pausa a contagem de toques por minuto
  }
  atualizarBotao(); // Atualiza o botão quando um toque é registrado
});

  // Atualiza o valor exibido no botão a cada segundo
  setInterval(function() {
    atualizarBotao();
  }, 1000);
  });