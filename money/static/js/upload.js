function submitNewAccount(formData, jqForm, options) { 

    var data = {};
    for (var i=0; i < formData.length; i++) { 
        data[formData[i].name] = formData[i].value
    } 
    $.ajax({
      url: "/api/accounts/"+data['modelid']+"/",
      headers: {
        'X-CSRFToken': data['csrfmiddlewaretoken'],
      },
      type: "PATCH",
      data: {
        'name': data['name'],
        'accounttype': data['accounttype'],
        'currency': data['currency'],
      },
      success:function(data) {
        console.log(data['id']);
        $("#account-body-"+data['id']).remove();
        console.log(data)
      },
    })
 
    // here we could return false to prevent the form from being submitted; 
    // returning anything other than false will allow the form submit to continue 
    return false; 
} 
