package com.example.SpringBootSample.domain.service.impl;

import com.example.SpringBootSample.domain.service.UserService;
import com.example.SpringBootSample.domain.user.model.MUser;
import com.example.SpringBootSample.repository.UserMapper;

import org.springframework.stereotype.Service;

@Service
public class UserServiceImpl implements UserService {

    private UserMapper mapper;

    // user signup
    @Override
    public void signup(MUser user) {
        user.setDepartmentId(1);
        user.setRole("ROLE_GENERAL");
        mapper.insertOne(user);

    }

}