package com.casa.springbootvalidacao.model;

import javax.validation.constraints.Email;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Pattern;

import com.casa.springbootvalidacao.validation.constraints.PlacaCarro;

import org.hibernate.validator.constraints.br.CPF;

import lombok.Data;

@Data
public class ClienteModel {

    private Integer id;

    @NotBlank(message = "Campo não informado")
    @Pattern(regexp = "^[A-Z]+(.)*", message = "Campo nome deve iniciar com letra maiuscula")
    private String nome;

    @Email(message = "Campo invalido")
    @NotBlank(message = "Campo não informado")
    private String email;

    @CPF(message = "Campo Invalido")
    @NotBlank(message = "Campo não informado")
    private String cpf;

    @NotBlank(message = "Campo não informado")
    @PlacaCarro(message = "Campo Inválido")
    private String placaCarro;

    @Min(value = 1900, message = "Ano de nascimento deve ser maior que 1900")
    private int anoNascimento;

}