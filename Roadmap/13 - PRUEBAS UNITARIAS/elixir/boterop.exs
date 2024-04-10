defmodule Boterop.Calculator do
  @spec sum(num1 :: number(), num2 :: number()) :: number()
  def sum(num1, num2) when is_number(num1) and is_number(num2) do
    num1 + num2
  end

  def sum(_num1, _num2), do: {:error, "Wrong input"}
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
      birth_date: Date.new(year, month, day),
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
end

ExUnit.start()

defmodule Boterop.UnitTest do
  use ExUnit.Case

  alias Boterop.Calculator
  alias Boterop.User

  describe "calculator" do
    test "sum/2 with valid numbers" do
      num1 = 5
      num2 = 45
      expected_result = 50
      result = Calculator.sum(num1, num2)

      assert expected_result == result
    end

    test "sum/2 with invalid params" do
      num1 = 5
      wrong_num2 = "Hi"
      {:error, _message} = Calculator.sum(num1, wrong_num2)
    end
  end

  describe "extra" do
    setup do
      %{
        user_struct: %User{},
        user: %User{
          name: "Botero P",
          age: 24,
          birth_date: [day: 9, month: 10, year: 1999],
          programming_languages: [:elixir, :python, :java]
        }
      }
    end

    test "all fields exist", %{user_struct: user} do
      assert Map.has_key?(user, :name)
      assert Map.has_key?(user, :age)
      assert Map.has_key?(user, :birth_date)
      assert Map.has_key?(user, :programming_languages)
    end

    test "compare created user", %{user: user} do
      expected_name = "Botero P"
      expected_age = 24
      expected_birth_date = [day: 9, month: 10, year: 1999]
      expected_programming_languages = [:elixir, :python, :java]

      %{
        name: ^expected_name,
        age: ^expected_age,
        birth_date: ^expected_birth_date,
        programming_languages: ^expected_programming_languages
      } = user
    end

    test "with wright data", %{user: user} do
      expected_user = %User{
        name: "Botero P",
        age: 24,
        birth_date: [day: 9, month: 10, year: 1999],
        programming_languages: [:elixir, :python, :java]
      }

      user_map = Map.from_struct(user)
      expected_user_map = Map.from_struct(expected_user)
      assert Map.equal?(user_map, expected_user_map)
      assert Map.equal?(user, expected_user)
    end

    test "with wrong data", %{user: user} do
      expected_user = %User{
        name: "Botero",
        age: 23,
        birth_date: [day: 9, month: 10, year: 1999],
        programming_languages: [:elixir, :python, :java]
      }

      user_map = Map.from_struct(user)
      refute Map.equal?(user_map, expected_user)
    end
  end
end
