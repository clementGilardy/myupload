$(function(){
    
    display_document("");

    $('button.new-folder').click(function(e){
        var newFolder = $('#folder-name').val();   
         $.ajax({
            type: "POST",
            url: "/upload/ajout-document",
            dataType: "json",
            traditional: true,
            data: {'name_folder': JSON.stringify(newFolder)},
            success: function(data){
            console.log(data['HTTPRESPONSE']);
                if(data['HTTPRESPONSE'])
                {
                 alertSuccess = '<div class="alert alert-success alert-dismissible"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><strong>Succès</strong> Dossier ajouté !</div>';
                $('.alert-doc').append(alertSuccess);

                }
                else
                {
                     alertError = '<div class="alert alert-danger alert-dismissible"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><strong>Attention</strong> Le dossier '+newFolder+' existe déjà</div>';
 
                $('.alert-doc').append(alertError);
                }
                display_document("");
            }
        });
    });

    $('.launchModal').click(function(e){
    e.preventDefault();
        $('#myModal').modal('show');
    });

    function display_document(id)
    {
        $('#folder').empty();
         $.ajax({
            type: "POST",
            url: "/upload/display-document",
            data: {'id_doc':JSON.stringify(id)},
            success: function(data){
                $.each(data["fileUser"], function(index,value){
                    realValue = value.toString().split(',');
                    divDoc = '<div style="width:50px;text-align:center;"><img height="50px" src="'+realValue[2]+'"/><br><a class="link-folder" href="">'+realValue[0]+'</a> </div>';
                    $('#folder').append(divDoc);

                    $('.link-folder').click(function(event){
                        event.preventDefault();
                       display_document(realValue[4]); 
                    });

                });
            },
            fail: function(){
                alert('fail');
            }
        });
    }

});



