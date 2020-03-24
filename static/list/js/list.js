$(document).ready(function() {
    $(':checkbox').on('click', changeTodoStatus);
  });

  function changeTodoStatus() {
    putNewStatus(this.getAttribute('data-todo-id'), $(this).is(':checked'));
  }
  

  var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

  function putNewStatus(todoID, isFinished) {
    $('#'+todoID).hide();
    $.ajax({
        url : '/api/list/' + todoID + '/',
        type : 'PATCH',
        headers:{"X-CSRFToken": $crf_token},
        contentType : 'application/json',
        xhr: function() {
            return window.XMLHttpRequest == null || new window.XMLHttpRequest().addEventListener == null 
                ? new window.ActiveXObject("Microsoft.XMLHTTP")
                : $.ajaxSettings.xhr();
        }
      });  

  }
  