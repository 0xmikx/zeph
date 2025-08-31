# zeph
catch-coin.html
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>Catch the Coin</title>
  <style>
    body {
      margin: 0; overflow: hidden;
      background: linear-gradient(to bottom, #0f1226, #1a1f3a);
      font-family: sans-serif; color: white;
    }
    #gameCanvas {
      display: block;
      margin: auto;
      background: #111;
      border: 2px solid #444;
    }
    #scoreboard {
      position: absolute; top: 10px; left: 10px;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <canvas id="gameCanvas" width="400" height="600"></canvas>
  <div id="scoreboard">Skor: 0 | Nyawa: 3</div>

  <script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');

    let player = { x: 180, y: 550, w: 40, h: 20 };
    let coin = { x: Math.random() * 360, y: 0, r: 10 };
    let score = 0;
    let lives = 3;
    let speed = 3;
    let keys = {};

    document.addEventListener('keydown', e => keys[e.key] = true);
    document.addEventListener('keyup', e => keys[e.key] = false);

    function update() {
      // Gerak player
      if (keys['ArrowLeft']) player.x -= 5;
      if (keys['ArrowRight']) player.x += 5;

      // Batas layar
      if (player.x < 0) player.x = 0;
      if (player.x + player.w > canvas.width) player.x = canvas.width - player.w;

      // Gerak coin
      coin.y += speed;

      // Tangkap
      if (
        coin.y + coin.r > player.y &&
        coin.x > player.x &&
        coin.x < player.x + player.w
      ) {
        score++;
        speed += 0.2;
        resetCoin();
      }

      // Miss
      if (coin.y > canvas.height) {
        lives--;
        resetCoin();
        if (lives <= 0) {
          alert('Game Over! Skor akhir: ' + score);
          score = 0; lives = 3; speed = 3;
        }
      }

      document.getElementById('scoreboard').textContent = `Skor: ${score} | Nyawa: ${lives}`;
    }

    function resetCoin() {
      coin.x = Math.random() * (canvas.width - 20);
      coin.y = 0;
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Player
      ctx.fillStyle = '#7aa2ff';
      ctx.fillRect(player.x, player.y, player.w, player.h);

      // Coin
      ctx.beginPath();
      ctx.arc(coin.x, coin.y, coin.r, 0, Math.PI * 2);
      ctx.fillStyle = '#ffd166';
      ctx.fill();
    }

    function loop() {
      update();
      draw();
      requestAnimationFrame(loop);
    }

    loop();
  </script>
</body>
</html>
