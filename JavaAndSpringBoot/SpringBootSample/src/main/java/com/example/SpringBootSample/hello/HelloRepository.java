package com.example.SpringBootSample.hello;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

@Repository
public class HelloRepository {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    public Map<String, Object> findById(String id) {
        String query = "Select * from employee where id = ?";

        Map<String, Object> employye = jdbcTemplate.queryForMap(query, id);

        return employye;
    }

}