function suma(a,b){
    return a+b;
}

test("Sum 2 + 2 equal 4",()=>{
    expect(suma.suma(2,2)).toBe(4)
});


let my_dict = {

    "name": "Raul",
    "age": "32",
    "birth_date": "11/09/1991",
    "programming_languages": ["Python","Javascript","Abap"]
};
test("Keys in object",()=>{

    expect("name" in suma.my_dict).toBeTruthy();
    expect("age" in suma.my_dict).toBeTruthy();
    expect("birth_date" in suma.my_dict).toBeTruthy();
    expect("programming_languages" in suma.my_dict).toBeTruthy();

});

test("Values for keys in object",()=>{

    expect(typeof(suma.my_dict["name"])).toBe("string");
    expect(typeof(suma.my_dict["age"])).toBe("string");
    expect(typeof(suma.my_dict["birth_date"])).toBe("string");
    expect(typeof(suma.my_dict["programming_languages"])).toBe("object")

});