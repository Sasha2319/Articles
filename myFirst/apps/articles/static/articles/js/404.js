$(document).mousemove(function (event) {
  $('.torch').css({
    'top': event.pageY,
    'left': event.pageX
  });
});
$(document).on("keydown", function(e){
  if(e.keyCode == 32){
    console.log("Пробел нажат");
    console.log(location.host + '    ' + location.protocol)
    window.location.href = `${location.protocol}//${location.host}`

  }
})
