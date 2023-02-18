function open_doc(myURL, title) {
  var myWidth = 1200;
  
  var myHeight=800;
  
  var left = (screen.width - myWidth) / 2;

  var top = (screen.height - myHeight) / 4;

  var myWindow = window.open(
    myURL,
    title,
    "toolbar=no, location=no, directories=no, status=no,menubar=no, scrollbars=yes, resizable=yes, copyhistory=no, width=" +
      myWidth +
      ", height=" +
      myHeight +
      ", top=" +
      top +
      ", left=" +
      left
  );
}
