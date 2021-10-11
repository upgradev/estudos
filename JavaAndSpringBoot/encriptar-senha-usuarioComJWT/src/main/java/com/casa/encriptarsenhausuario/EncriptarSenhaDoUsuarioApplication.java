package com.casa.encriptarsenhausuario;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration;
import org.springframework.context.annotation.Bean;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

// Para não validar o usuario e senha exclude = {SecurityAutoConfiguration.class}
// @SpringBootApplication(exclude = { SecurityAutoConfiguration.class })
@SpringBootApplication()
public class EncriptarSenhaDoUsuarioApplication {

	public static void main(String[] args) {
		SpringApplication.run(EncriptarSenhaDoUsuarioApplication.class, args);

	}

	@Bean
	public PasswordEncoder getPasswordEncoder() {
		BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
		return encoder;
	}

}
