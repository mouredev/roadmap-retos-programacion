import org.json.JSONArray
import org.json.JSONObject
import java.io.File
import javax.xml.parsers.DocumentBuilderFactory
import javax.xml.transform.TransformerFactory
import javax.xml.transform.dom.DOMSource
import javax.xml.transform.stream.StreamResult
import org.w3c.dom.Document

data class Person(
    val name: String,
    val age: Int,
    val birthDate: String,
    val programmingLanguages: List<String>
)

fun main() {
    val person = Person("EulogioEP", 41, "1981-05-07", listOf("Kotlin", "Java", "Python"))

    createXMLFile(person)
    createJSONFile(person)

    println("XML content:")
    println(File("person.xml").readText())
    
    println("\nJSON content:")
    println(File("person.json").readText())

    // Delete files
    File("person.xml").delete()
    File("person.json").delete()

    println("\nFiles deleted.")

    // Extra challenge
    val xmlPerson = readXMLFile("person.xml")
    val jsonPerson = readJSONFile("person.json")

    println("\nPerson from XML: $xmlPerson")
    println("Person from JSON: $jsonPerson")
}

fun createXMLFile(person: Person) {
    val docFactory = DocumentBuilderFactory.newInstance()
    val docBuilder = docFactory.newDocumentBuilder()
    val doc: Document = docBuilder.newDocument()

    val rootElement = doc.createElement("person")
    doc.appendChild(rootElement)

    val name = doc.createElement("name")
    name.appendChild(doc.createTextNode(person.name))
    rootElement.appendChild(name)

    val age = doc.createElement("age")
    age.appendChild(doc.createTextNode(person.age.toString()))
    rootElement.appendChild(age)

    val birthDate = doc.createElement("birthDate")
    birthDate.appendChild(doc.createTextNode(person.birthDate))
    rootElement.appendChild(birthDate)

    val languages = doc.createElement("programmingLanguages")
    person.programmingLanguages.forEach {
        val lang = doc.createElement("language")
        lang.appendChild(doc.createTextNode(it))
        languages.appendChild(lang)
    }
    rootElement.appendChild(languages)

    val transformerFactory = TransformerFactory.newInstance()
    val transformer = transformerFactory.newTransformer()
    val source = DOMSource(doc)
    val result = StreamResult(File("person.xml"))
    transformer.transform(source, result)
}

fun createJSONFile(person: Person) {
    val json = JSONObject()
    json.put("name", person.name)
    json.put("age", person.age)
    json.put("birthDate", person.birthDate)
    json.put("programmingLanguages", JSONArray(person.programmingLanguages))

    File("person.json").writeText(json.toString(2))
}

fun readXMLFile(filename: String): Person {
    val file = File(filename)
    val dbFactory = DocumentBuilderFactory.newInstance()
    val dBuilder = dbFactory.newDocumentBuilder()
    val doc = dBuilder.parse(file)
    doc.documentElement.normalize()

    val name = doc.getElementsByTagName("name").item(0).textContent
    val age = doc.getElementsByTagName("age").item(0).textContent.toInt()
    val birthDate = doc.getElementsByTagName("birthDate").item(0).textContent
    val languagesNodes = doc.getElementsByTagName("language")
    val languages = (0 until languagesNodes.length).map { languagesNodes.item(it).textContent }

    return Person(name, age, birthDate, languages)
}

fun readJSONFile(filename: String): Person {
    val jsonString = File(filename).readText()
    val json = JSONObject(jsonString)

    val name = json.getString("name")
    val age = json.getInt("age")
    val birthDate = json.getString("birthDate")
    val languages = json.getJSONArray("programmingLanguages").let {
        (0 until it.length()).map { i -> it.getString(i) }
    }

    return Person(name, age, birthDate, languages)
}