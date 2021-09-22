package com.example.SpringBootSample.hello;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class HelloService {

    @Autowired
    private HelloRepository repository;

    public Employee getEmployee(String id){
        // search
        Map<String, Object> map = repository.findById(id);

        // get value from map
        String employeeId = (String) map.get("id");
        String name = (String) map.get("name");
        int age = (int) map.get("age");

        // set the employee class toa  value
        Employee employee = new Employee();
        employee.setEmployeeId(employeeId);
        employee.setEmployeeName(name);
        employee.setEmployeeAge(age);

        return employee;
    }
}