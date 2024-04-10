defmodule Boterop.JSON do
  @spec encode(map :: map()) :: String.t()
  def encode(%{} = map) do
    json =
      map
      |> Map.from_struct()
      |> Enum.map(fn {k, v} -> format(k, v) end)
      |> Enum.join("\n\t")

    "{\n\t#{json}\n}"
  end

  @spec decode(json_string :: String.t()) :: map()
  def decode(json_string) do
    json_string
    |> String.split("\n")
    |> Enum.map(fn v -> Regex.replace(~r/\\|\n|\t|\"/, v, "") end)
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
    do: "#{format_key(k)}: [\"#{Enum.join(list, "\", \"")}\"]"

  defp format(k, text), do: "#{format_key(k)}: \"#{text}\""

  @spec format_key(k :: String.t()) :: String.t()
  def format_key(k), do: "\"#{k}\""
end

defmodule Boterop.XML do
  @spec encode(map :: map()) :: String.t()
  def encode(%{} = map) do
    xml =
      map
      |> Map.from_struct()
      |> Enum.map(fn {k, v} -> format(k, v) end)
      |> Enum.join("\n")

    xml_start = ~S(<?xml version="1.0" encoding="UTF-8"?>)
    xml_start <> "\n#{xml}"
  end

  @spec decode(xml_string :: String.t()) :: map()
  def decode(xml_string) do
    xml_string
    |> String.split("\n")
    |> Enum.map(fn v -> Regex.replace(~r/\\|\n|\t|\"/, v, "") end)
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
  defp format(k, [_head | _tail] = list) do
    singular_k =
      k
      |> Atom.to_string()
      |> (&Regex.replace(~r/s$/, &1, "")).()

    start_singular = format_key(singular_k)
    end_singular = format_end_key(singular_k)

    "#{format_key(k)}\n\t#{start_singular}#{Enum.join(list, "#{end_singular}\n\t#{start_singular}")}#{end_singular}\n#{format_key(k)}"
  end

  defp format(k, text), do: "#{format_key(k)}#{text}#{format_end_key(k)}"

  @spec format_key(k :: String.t()) :: String.t()
  def format_key(k), do: "<#{k}>"

  @spec format_end_key(k :: String.t()) :: String.t()
  def format_end_key(k), do: "</#{k}>"
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

user
|> Boterop.JSON.encode()
|> Boterop.JSON.decode()
|> Boterop.User.from_map()
|> Boterop.XML.encode()
|> IO.puts()
