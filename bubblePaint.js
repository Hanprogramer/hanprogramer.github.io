// bubble-paint.js
registerPaint('randomBackground', class {
    paint(ctx, geom) {
      var rectSize = 36;
      for(var x = 0; x < geom.width; x += rectSize)
      for(var y = 0; y < geom.height; y += rectSize){
        /// Fill in random block
        ctx.fillStyle = getRandomHexColor();
        ctx.fillRect(x, y, rectSize, rectSize);
      }
    
    }
  })
  
  function getRandomHexColor() {
      var arr = ["rgb(14, 14, 14)","rgb(20, 20, 20)", "rgb(24, 24, 24)"];
    return arr[Math.floor(Math.random() * arr.length)]; 
  }