defmodule Boterop.JSON do
  def encode(%{} = map) do
    json =
      map
      |> Map.from_struct()
      |> Enum.map(fn {k, v} -> format(k, v) end)
      |> Enum.join("\n\t")

    "{\n\t#{json}\n}"
  end

  def decode(json_string) do
    json_string
    |> String.split("\n")
    |> Enum.map(fn v -> Regex.replace(~r/\\|\n|\t|\"/, v, "") end)
    |> List.delete_at(0)
    |> List.delete_at(-1)
    |> to_map()
  end

  def to_map(list, map \\ %{})
  def to_map([], map), do: map

  def to_map([head | tail], map) do
    [key | [value]] = String.split(head, ":")
    key = String.to_atom(key)
    value = value |> String.trim() |> format_value()
    new_map = Map.put(map, key, value)

    to_map(tail, new_map)
  end

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
      {_num, "-" <> _rest} -> format_date(text)
      {_num, _decimals} -> text
    end
  end

  defp format_date(text) do
    [year | [month | [day]]] =
      text
      |> String.split("-")
      |> Enum.map(fn text -> String.to_integer(text) end)

    Date.new!(year, month, day)
  end

  defp format(k, [_head | _tail] = list), do: "\"#{k}\": [\"#{Enum.join(list, "\", \"")}\"]"
  defp format(k, %Date{} = date), do: "\"#{k}\": \"#{date}\""
  defp format(k, text), do: "\"#{k}\": \"#{text}\""
end

defmodule Boterop.User do
  @type t :: %__MODULE__{
          name: String.t(),
          age: integer(),
          birth_date: Date.t(),
          programming_languages: list(atom())
        }

  defstruct [:name, :age, :birth_date, :programming_languages]

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

  def from_map(%{} = map), do: struct(__MODULE__, map)
end

user = Boterop.User.new("boterop", 24, [day: 9, month: 10, year: 1999], [:elixir, :python])

user
|> Boterop.JSON.encode()
|> Boterop.JSON.decode()
|> Boterop.User.from_map()
|> IO.inspect()
