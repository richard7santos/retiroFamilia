$(document).ready( function () {
    $('#list-insc').DataTable(
        {
        info: false,
        paging: false,
        searching: false
        }
    );

    function limpa_formulário_cep() {
        $("#id_logradouro").val("");
        $("#id_bairro").val("");
        $("#id_cidade").val("");
        $("#id_uf").val("");
    }

    $("#id_cep").blur(function() {

        var cep = $(this).val().replace(/\D/g, '');

        if (cep != "") {
            var validacep = /^[0-9]{8}$/;

            if(validacep.test(cep)) {
                $("#id_logradouro").val("aguardando dados...");
                $("#id_bairro").val("aguardando dados...");
                $("#id_cidade").val("aguardando dados...");
                $("#id_uf").val("aguardando dados...");

                $.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {

                    if (!("erro" in dados)) {
                        $("#id_logradouro").val(dados.logradouro);
                        $("#id_bairro").val(dados.bairro);
                        $("#id_cidade").val(dados.localidade);
                        $("#id_uf").val(dados.uf);
                    } 
                    else {
                        limpa_formulário_cep();
                        alert("CEP não encontrado.");
                    }
                });
            } 
            else {
                limpa_formulário_cep();
                alert("Formato de CEP inválido.");
            }
        } 
        else {
            limpa_formulário_cep();
        }
    });

    $("#id_nome_inscrito").attr("placeholder", "Informe seu nome completo");
    $("#id_email").attr("placeholder", "email@email.com");
    $("#id_complemento").attr("placeholder", "Ex. Apt X, bloco Y...");
    $("#id_username").attr("placeholder", "Informe seu usuário");
    $("#id_password").attr("placeholder", "Informe sua senha");
    $("#id_password1").attr("placeholder", "Escolha uma senha segura");
    $("#id_password2").attr("placeholder", "Repita a sua senha segura");
    $('#id_telefone_1').mask('(00) 00000-0000', {placeholder: "(xx) xxxxx-xxxxx"});
    $('#id_telefone_2').mask('(00) 00000-0000', {placeholder: "(xx) xxxxx-xxxxx"});
    $('#id_cep').mask('00000-000', {placeholder: "xxxxx-xxx"});
    $('#id_dt_inscricao').mask('00/00/0000 00:00:00');
    $('#id_data_pagamento').mask('00/00/0000');
    
} );

$(function(){
    $('.payment-form').formset({

        addText: 'Registrar novo pagamento',
        deleteText: 'Remover este Pagamento',
    });
})
