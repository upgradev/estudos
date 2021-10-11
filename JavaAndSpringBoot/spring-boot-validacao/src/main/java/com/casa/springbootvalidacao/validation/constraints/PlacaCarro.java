package com.casa.springbootvalidacao.validation.constraints;

import java.lang.annotation.Documented;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

import javax.validation.Constraint;
import javax.validation.Payload;

import com.casa.springbootvalidacao.validation.PlacaCarroValidation;

@Documented
@Constraint(validatedBy = PlacaCarroValidation.class)
@Target({ ElementType.METHOD, ElementType.FIELD })
@Retention(RetentionPolicy.RUNTIME)
public @interface PlacaCarro {

    String message() default "Placa de carro inválida";

    Class<?>[] groups() default {}; //padrão validacao

    Class<? extends Payload>[] payload() default {}; //padrão validacao

}