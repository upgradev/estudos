package com.example.SpringBootSample.repository;

import com.example.SpringBootSample.domain.user.model.MUser;

import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface UserMapper {

    // user signup
    public int insertOne(MUser user);
}