package com.casa.encriptarsenhausuario.service;

import java.util.Optional;

import com.casa.encriptarsenhausuario.data.DetalheUsuarioData;
import com.casa.encriptarsenhausuario.model.UsuarioModel;
import com.casa.encriptarsenhausuario.repository.UsuarioRepository;

import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Component;

@Component
public class DetalheUsuarioServiceImpl implements UserDetailsService {

    private final UsuarioRepository repository;

    public DetalheUsuarioServiceImpl(UsuarioRepository repository) {
        this.repository = repository;
    }

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {

        Optional<UsuarioModel> usuario = repository.findByLogin(username);
        if (usuario.isEmpty()) {
            throw new UsernameNotFoundException("Usuario [ " + usuario + "] não encontrado");
        }

        return new DetalheUsuarioData(usuario);
    }

}