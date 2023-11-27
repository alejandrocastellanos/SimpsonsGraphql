from pytest import mark


@mark.asyncio
async def test_query_character_description(graph_client, graphql_context_fixture):
    query = '''
        query {
          characterDescription(name: "bart") {
            name
            story
            image
            gender
            status
            occupation
          }
        }
    '''
    result = await graph_client.execute_async(query, context=graphql_context_fixture)

    assert result == {
        "data": {
            "characterDescription": [
                {
                    "name": "Bart Simpson",
                    "story": "conocido como El Barto y Bartman , es el hijo mayor travieso, rebelde, incomprendido y potencialmente peligroso de Homer y Marge Simpson, y el hermano de Lisa y Maggie Simpson\r\n",
                    "image": "https://static.simpsonswiki.com/images/e/ef/Tapped_Out_Unlock_Bart.png",
                    "gender": "Masculino",
                    "status": "Vivo",
                    "occupation": "Estudiante en la Escuela primaria de Springfield"
                },
                {
                    "name": "Ciborg Bart",
                    "story": "Cyborg Bart era en lo que se convirtió Bart Simpson después de recolectar partes de robots para convertirse en un poderoso cyborg.",
                    "image": "https://static.simpsonswiki.com/images/thumb/7/7f/TSTO_Cyborg_Bart.png/250px-TSTO_Cyborg_Bart.png",
                    "gender": "Masculino",
                    "status": "Robot",
                    "occupation": "Robot"
                },
                {
                    "name": "Bart del Futuro",
                    "story": "Bart del futuro",
                    "image": "https://res.cloudinary.com/dglqojivj/image/upload/v1682726683/simpsons/61px-Mooch_Bart_wphfmj.png",
                    "gender": "Masculino",
                    "status": "Vivo",
                    "occupation": "Desocupado"
                },
                {
                    "name": "Chirpy Boy y Bart Junior",
                    "story": "Chirpy Boy y Bart Junior son lagartos de árboles bolivianos a los que Bart nombró.",
                    "image": "https://static.simpsonswiki.com/images/thumb/2/26/Chirpy_Boy_and_Bart_Junior.png/250px-Chirpy_Boy_and_Bart_Junior.png",
                    "gender": "Masculino",
                    "status": "Vivo",
                    "occupation": "Mascota"
                }
            ]
        }
    }


@mark.asyncio
async def test_query_character_list(graph_client, graphql_context_fixture):
    query = '''
        query {
          characterList(page: 1, limit: 1) {
            name
            occupation
          }
        }

    '''
    result = await graph_client.execute_async(query, context=graphql_context_fixture)

    assert result == {
        "data": {
            "characterList": [
                {
                    "name": "Marge Simpson",
                    "occupation": "Ama de casa"
                }
            ]
        }
    }
