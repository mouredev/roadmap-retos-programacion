defmodule Boterop.JSON do
  @type json :: String.t()

  @spec encode(map :: map()) :: json()
  def encode(%{} = map) do
    json =
      map
      |> Map.from_struct()
      |> Enum.map(fn {k, v} -> format(k, v) end)
      |> Enum.join("\n\t")
      |> String.slice(0..-2//1)

    "{\n\t#{json}\n}"
  end

  @spec decode(json_string :: json()) :: map()
  def decode(json_string) do
    json_string
    |> String.split("\n")
    |> Enum.map(fn v -> Regex.replace(~r/\\|\n|\t|\"|,+$/, v, "") end)
    |> List.delete_at(0)
    |> List.delete_at(-1)
    |> to_map()
  end

  @spec to_map(list :: list(String.t()), map :: map()) :: map()
  defp to_map(list, map \\ %{})
  defp to_map([], map), do: map

  defp to_map([head | tail], map) do
    [key | [value]] = String.split(head, ":")
    key = String.to_atom(key)
    value = value |> String.trim() |> format_value()
    new_map = Map.put(map, key, value)

    to_map(tail, new_map)
  end

  @spec format_value(text :: String.t()) :: String.t() | integer()
  defp format_value("[" <> text) do
    text
    |> String.replace("]", "")
    |> String.split(",")
    |> Enum.map(fn v -> v |> String.trim() end)
  end

  defp format_value(text) do
    case Integer.parse(text) do
      :error -> text
      {num, ""} -> num
      {_num, _decimals} -> text
    end
  end

  @spec format(k :: String.t(), list(String.t()) | Date.t() | String.t()) :: String.t()
  defp format(k, [_head | _tail] = list),
    do: "#{format_key(k)}: [\"#{Enum.join(list, "\", \"")}\"],"

  defp format(k, text), do: "#{format_key(k)}: \"#{text}\","

  @spec format_key(k :: String.t()) :: String.t()
  defp format_key(k), do: "\"#{k}\""
end

defmodule Boterop.XML do
  @type xml :: String.t()

  @spec encode(map :: map()) :: xml()
  def encode(%{} = map) do
    xml =
      map
      |> Map.from_struct()
      |> Enum.map(fn {k, v} -> format(k, v) end)
      |> Enum.join("\n")

    xml_start = ~S(<?xml version="1.0" encoding="UTF-8"?>)
    xml_start <> "\n#{create_block("item", xml, "\n")}"
  end

  @spec decode(xml_string :: xml()) :: map()
  def decode(xml_string) do
    map =
      xml_string
      |> String.split("\n")
      |> List.delete_at(0)
      |> List.delete_at(0)
      |> List.delete_at(-1)
      |> List.delete_at(-1)
      |> Enum.map(fn v -> Regex.replace(~r/<\/[a-zA-Z_]+>/, v, "") end)
      |> Enum.map(fn v -> Regex.replace(~r/<item>|\t/, v, "") end)
      |> Enum.map(fn v -> Regex.replace(~r/</, v, "") end)
      |> Enum.map(fn v -> Regex.replace(~r/>/, v, ":") end)

    lists =
      map
      |> Enum.filter(fn v -> Regex.match?(~r/.*:$/, v) end)
      |> Enum.map(fn v -> Regex.replace(~r/:/, v, "") end)
      |> Enum.map(fn v -> singularize(v) end)

    map
    |> Enum.filter(fn v -> not Regex.match?(~r/.*:$/, v) end)
    |> Enum.map(fn v -> String.trim(v) end)
    |> join_lists(lists)
    |> to_map()
  end

  @spec join_lists(list :: list(String.t()), list(String.t())) :: list(String.t())
  defp join_lists(list, []), do: list

  defp join_lists(list, [head | tail]) do
    plural_k = head <> "s"

    list_data =
      list
      |> Enum.filter(fn v -> String.contains?(v, head) end)
      |> Enum.map(fn v -> Regex.replace(~r/^.*?:/, v, "") end)
      |> Enum.join(", ")

    list
    |> Enum.filter(fn v -> not String.contains?(v, head) end)
    |> Enum.concat(["#{plural_k}: [#{list_data}]"])
    |> join_lists(tail)
  end

  @spec to_map(list :: list(String.t()), map :: map()) :: map()
  defp to_map(list, map \\ %{})
  defp to_map([], map), do: map

  defp to_map([head | tail], map) do
    [key | [value]] = String.split(head, ":")
    key = String.to_atom(key)
    value = value |> String.trim() |> format_value()
    new_map = Map.put(map, key, value)

    to_map(tail, new_map)
  end

  @spec format_value(text :: String.t()) :: String.t() | integer()
  defp format_value("[" <> text) do
    text
    |> String.replace("]", "")
    |> String.split(",")
    |> Enum.map(fn v -> v |> String.trim() end)
  end

  defp format_value(text) do
    case Integer.parse(text) do
      :error -> text
      {num, ""} -> num
      {_num, _decimals} -> text
    end
  end

  @spec format(k :: String.t(), list(String.t()) | Date.t() | String.t()) :: String.t()
  defp format(k, [_head | _tail] = list) do
    singular_k =
      k
      |> Atom.to_string()
      |> singularize()

    list_block = create_block(singular_k, list)
    create_block(k, list_block, "\n")
  end

  defp format(k, text), do: create_block(k, text)

  @spec create_block(
          k :: String.t(),
          v :: String.t(),
          separator :: String.t()
        ) :: String.t()
  defp create_block(k, list, separator \\ "")

  defp create_block(k, list, _separator) when is_list(list) do
    block =
      list
      |> Enum.join("#{format_end_key(k)}\n\t#{format_key(k)}")

    "\t#{format_key(k)}#{block}#{format_end_key(k)}"
  end

  defp create_block(k, v, separator) do
    block =
      v
      |> to_string()
      |> String.contains?("\n")
      |> if do
        v
        |> String.split("\n")
        |> Enum.map(fn value -> "\t#{value}" end)
        |> Enum.join("\n")
      else
        v
      end

    "#{format_key(k)}#{separator}#{block}#{separator}#{format_end_key(k)}"
  end

  @spec singularize(text :: String.t()) :: String.t()
  defp singularize(text), do: Regex.replace(~r/s$/, text, "")

  @spec format_key(k :: String.t()) :: String.t()
  defp format_key(k), do: "<#{k}>"

  @spec format_end_key(k :: String.t()) :: String.t()
  defp format_end_key(k), do: "</#{k}>"
end

defmodule Boterop.User do
  @type t :: %__MODULE__{
          name: String.t(),
          age: integer(),
          birth_date: Date.t(),
          programming_languages: list(atom())
        }

  defstruct [:name, :age, :birth_date, :programming_languages]

  @spec new(
          name :: String.t(),
          age :: integer(),
          birth_date :: Date.t() | [day: integer(), month: integer(), year: integer()],
          programming_languages :: list(atom())
        ) :: __MODULE__.t()
  def new(name, age, birth_date, programming_languages) when is_list(birth_date) do
    day = Keyword.get(birth_date, :day)
    month = Keyword.get(birth_date, :month)
    year = Keyword.get(birth_date, :year)

    %__MODULE__{
      name: name,
      age: age,
      birth_date: Date.new!(year, month, day),
      programming_languages: programming_languages
    }
  end

  def new(name, age, birth_date, programming_languages) do
    %__MODULE__{
      name: name,
      age: age,
      birth_date: birth_date,
      programming_languages: programming_languages
    }
  end

  @spec from_map(map :: map()) :: __MODULE__.t()
  def from_map(%{} = map) do
    __MODULE__
    |> struct(map)
    |> format_date()
  end

  @spec format_date(user :: __MODULE__.t()) :: __MODULE__.t()
  defp format_date(%__MODULE__{birth_date: text} = user) do
    [year | [month | [day]]] =
      text
      |> String.split("-")
      |> Enum.map(fn text -> String.to_integer(text) end)

    date = Date.new!(year, month, day)
    %__MODULE__{user | birth_date: date}
  end
end

user = Boterop.User.new("boterop", 24, [day: 9, month: 10, year: 1999], [:elixir, :python])

path = Regex.replace(~r/\/[^\/]+$/, __ENV__.file, "")

# Write user.json file
user
|> Boterop.JSON.encode()
|> (&File.write("#{path}/user.json", &1)).()

# Write user.xml file
user
|> Boterop.XML.encode()
|> (&File.write("#{path}/user.xml", &1)).()

# Extra

# Read user.json and print the %User{} info
"#{path}/user.json"
|> File.read!()
|> Boterop.JSON.decode()
|> Boterop.User.from_map()
|> IO.inspect()

# Read user.xml and print the %User{} info
"#{path}/user.xml"
|> File.read!()
|> Boterop.XML.decode()
|> Boterop.User.from_map()
|> IO.inspect()

# Remove files
File.rm_rf("#{path}/user.json")
File.rm_rf("#{path}/user.xml")
