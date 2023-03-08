<!DOCTYPE html>
<html>
    <title>API</title>
<body>
    <style>
        fieldset {
            border-radius: 5px;
            border-color: black;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 30%;
        }

        input {
            border: 1px solid #dadce0;
		    border-radius: 4px;
		    box-shadow: 0 0 0 transparent;
		    font-size: 16px;
		    line-height: 24px;
		    outline: transparent;
		    padding: 11px 16px;
		    width: 92%;
		    outline: none;
		    letter-spacing: 1px;
        }

        .button {
            width: 100%;
            color: blueviolet;
            cursor: pointer;
        }

        body {
            background-color: royalblue;
        }
    </style>
    <fieldset>
        <form method="post"  action="{{url_for('index')}}">
            <label>Nome</label>
            <br>
            <input type="text" name="name">
            <br>
            <br>
            <label>Posição do Rosto</label>
            <br>
            <input type="text" name="rosto">
            <br>
            <br>
            <label>Link Imagem</label>
            <br>
            <input type="text" name="imagem">
            <br>
            <br>
            <label>Brasão</label>
            <br>
            <input type="text" name="brasão">
            <br>
            <br>
            <label>Skills</label>
            <br>
            <input type="text" name="skills">
            <br>
            <br>
            <input class="button" type="submit">
        </form>
    </fieldset>
</body>
</html>
