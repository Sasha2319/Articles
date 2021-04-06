console.log("Hello world");
    const form = document.getElementById("cmForm");
    const comment_author = document.getElementById("id_comment_author");
    const comment_text = document.getElementById("id_comment_text");
    const csrf = document.getElementsByName("csrfmiddlewaretoken");
    const token = csrf[0].value




    fr=form.addEventListener("submit", e=>{
        e.preventDefault()
        const fd = new FormData()
        fd.append('csrfmiddlewaretoken', token)
        fd.append('comment_author', comment_author.value)
        fd.append('comment_text', comment_text.value)

        $.ajax({
            type: 'POST',
            url: url,
            enctype: 'multipart/form-data',
            data: fd,
            processData: false,
            success: function(response){
                console.log(response)
                $(` <div class="d-flex flex-column comment-section" style="margin-top:10px;">
                <div class="bg-white p-2">
                    <div class="d-flex flex-row user-info"><img class="rounded-circle" src=${avatar_url} width="40">
                        <div class="d-flex flex-column justify-content-start ml-2"><span class="d-block font-weight-bold name">${response.comment_author}</span><span class="date text-black-50">Shared publicly - ${response.cDate}</span></div>
                    </div>
                    <div class="mt-2">
                        <p class="comment-text">${response.comment_text}</p>
                    </div>
                </div>
                <div class="bg-white">
                    <div class="d-flex flex-row fs-12">

                    </div>
                </div>
               
            </div>`).insertAfter("#cmForm");
            $("input").val("")
            $("textarea").val("")
                
            },
            cache: false,
            contentType: false, 
        })
    })