package io.github.upgradev;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import io.github.upgradev.domain.entity.Cliente;
import io.github.upgradev.domain.repositorio.Clientes;

@SpringBootApplication
// @ComponentScan(basePackages = { "io.github.upgradev.repository",
// "io.github.upgradev.service" })
public class VendasApplication {

	@Bean
	public CommandLineRunner init(@Autowired Clientes clientes) {
		return args -> {
			System.out.println("Salvando clientes");
			clientes.salvar(new Cliente("Cleison"));
			clientes.salvar(new Cliente("Ana"));

			List<Cliente> obterTodos = clientes.obterTodos();
			obterTodos.forEach(System.out::println);

			System.out.println("Atualizando clientes");
			obterTodos.forEach(c -> {
				c.setNome(c.getNome() + " Atualizado");
				clientes.atualizar(c);
			});

			System.out.println("Buscando clientes");
			clientes.buscarPorNome("Cle").forEach(System.out::println);


			// obterTodos = clientes.obterTodos();
			// obterTodos.forEach(System.out::println);
			

		};
	}

	public static void main(String[] args) {
		SpringApplication.run(VendasApplication.class, args);
	}

}
