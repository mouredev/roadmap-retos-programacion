import { assert,test } from 'poku'; //libreria usada para el testing
function sum(x:number,y:number):number {
  if(typeof x !=='number'|| typeof y !=='number' ){
   return assert.fail('they not are numbers...')
  }
  return x + y
}
class TestSum{
  constructor(){}
   trySumTest(sum:(x:any,y:any)=>number){
    test('Testing "sum" method', () => {
      assert.strictEqual(sum(0, 0), 0, 'should return zero');
      assert.strictEqual(sum(0, 1), 1, 'should return one');
      assert.strictEqual(sum(1, 1), 2, 'should return two');
      assert.strictEqual(sum(1, '1a'), 2, 'should return two');//con esto comprobamos errores de tipo
    });
  }
}
 const tester = new TestSum();//aqui mandamos llamar a la clase y hacemos pruebas->
 tester.trySumTest(sum)
class TesterExtra{
  private _data :{[key: string]: any}={}
  constructor(name?:any,age?:any,birth_date?:any,programming_languages?:any){
    this._data.name = name
    this._data.age = Number(age)
    this._data.birth_date = new Date(birth_date)
    this._data.programming_languages = programming_languages
  }
  ifAllExistTest(){
    test('All exist?', () => {
      assert.equal(true, Object.hasOwn(this._data,'name'),'test has name ok!');
      assert.equal(true, Object.hasOwn(this._data,'age'),'test has age ok!');
      assert.equal(true, Object.hasOwn(this._data,'birth_date'),'test has date ok!');
      assert.equal(true, Object.hasOwn(this._data,'programming_languages'),'test has languages ok!');
    });
  }
  typesAreOkTest(){
    test('All types ok?', () => {
      assert.equal(typeof this._data.name, 'string','test name is string?');
      assert.equal(!isNaN(this._data.age),true,'test age is number?');
      assert.equal(!isNaN(this._data.birth_date.getTime()), true,'test birth_date is date?');
      assert.equal(Array.isArray(this._data.programming_languages),true,'test languages is Array?');
    });
  }
  toString(){
    console.log(this._data)
  }
}
const testerExtra = new TesterExtra('david','24','2024-12-31',['js','typescript','react'])
testerExtra.toString()
testerExtra.ifAllExistTest()
testerExtra.typesAreOkTest()

