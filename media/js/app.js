function reply_click(clicked_id)
  {
      if (confirm('Você quer mesmo apagar?')) {

        $.ajax({
          url: '/superheros/' + clicked_id,
          method: 'delete',
          dataType: 'json',
          success: function (parametrosMaquina) {

          console.log("passou pelo delete")

          $.ajax({
          url: '/superheros/',
          method: 'get',
          dataType: 'json',
          success: function (superheros) {
                 console.log(superheros.super_hero)

                 $("#tabela tr").remove();

                tags =  "<tr >" +
                    "<th> Nome </th>" +
                    "<th>" + "Descrição" + "</th>" +
                    "<th>" + "Foto" + "</th>" +
                    "<th>" + "Opções" + "</th>" +
                    "</tr>"


                superheros.super_hero.forEach(function(hero){

                    tags = tags +
                    "<tr>"+
                    "<th>"+ hero.name+"</th>"+
                    "<th>"+ hero.description+"</th>"+
                    "<th><img src="+ hero.photo+" border=3 height=100 width=100></img></th>"+
                    "<th><button type= button id= deletar onClick= reply_click("+ hero.id +")> Deletar</button></th>"+
                    "</tr>"

                })

               var tableBody = $("#tabela tbody");
               tableBody.append(tags);


           }
        });

           }
        });

       }
  }


function search()
  {

        if($('#search_box').val() == ""){

        $.ajax({
          url: '/superheros/',
          method: 'get',
          dataType: 'json',
          success: function (superheros) {
                 console.log(superheros.super_hero)

                 $("#tabela tr").remove();

                tags =  "<tr >" +
                    "<th> Nome </th>" +
                    "<th>" + "Descrição" + "</th>" +
                    "<th>" + "Foto" + "</th>" +
                    "<th>" + "Opções" + "</th>" +
                    "</tr>"


                superheros.super_hero.forEach(function(hero){

                    tags = tags +
                    "<tr>"+
                    "<th>"+ hero.name+"</th>"+
                    "<th>"+ hero.description+"</th>"+
                    "<th><img src="+ hero.photo+" border=3 height=100 width=100></img></th>"+
                    "<th><button type= button id= deletar onClick= reply_click("+ hero.id +")> Deletar</button></th>"+
                    "</tr>"

                })

               var tableBody = $("#tabela tbody");
               tableBody.append(tags);


           }
        });
        }else{
         data={
            name:$('#search_box').val()
        }

        $.ajax({
          url: '/findsuperhero/',
          method: 'post',
          dataType: 'json',
          data: data,
          success: function (hero) {
                console.log(hero.super_hero)
                $("#tabela tr").remove();

                tags =  "<tr >" +
                    "<th> Nome </th>" +
                    "<th>" + "Descrição" + "</th>" +
                    "<th>" + "Foto" + "</th>" +
                    "<th>" + "Opções" + "</th>" +
                    "</tr>"


                    tags = tags +
                    "<tr>"+
                    "<th>"+ hero.super_hero.name+"</th>"+
                    "<th>"+ hero.super_hero.description+"</th>"+
                    "<th><img src="+ hero.super_hero.photo+" border=3 height=100 width=100></img></th>"+
                    "<th><button type= button id= deletar onClick= reply_click("+ hero.super_hero.id +")> Deletar</button></th>"+
                    "</tr>"

               var tableBody = $("#tabela tbody");
               tableBody.append(tags);

          }

          })
        }


  }



