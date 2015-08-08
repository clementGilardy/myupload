$(function(){
    

    $('button.new-folder').click(function(e){
        var newFolder = $('#folder-name').val();   
        var idParent  = $('input.parent').val();
         $.ajax({
            type: "POST",
            url: "/upload/ajout-document",
            dataType: "json",
            traditional: true,
            data: {'name_folder': JSON.stringify(newFolder),'id_parent':JSON.stringify(idParent)},
            success: function(data){
                if(data['response'])
                {
                 alertSuccess = '<div class="alert alert-success alert-dismissible"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><strong>Succès</strong> Dossier ajouté !</div>';
                $('.alert-doc').append(alertSuccess);
                
                 var divDoc = '<div class="link-folder" style="display:inline-block;margin-left:9px;text-align:center"> <img style="height:50px" src="'+data['icon']+'" alt="'+data['name']+'"/><br> <a class="link-folder" href="/upload/documents/'+data['id']+'",id="'+data['id']+'">'+data['name']+'</a></div>';

                 $('div#folder').append(divDoc);


                }
                else
                {
                     alertError = '<div class="alert alert-danger alert-dismissible"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><strong>Attention</strong> Le dossier '+newFolder+' existe déjà</div>';
 
                $('.alert-doc').append(alertError);
                }
            }
        });
    });

    $('.launchModal').click(function(e){
        e.preventDefault();
        $('#myModal').modal('show');
    });
});



