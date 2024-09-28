defmodule Boterop.Regex do
  @spec get_numbers(text :: String.t()) :: list(String.t()) | nil
  def get_numbers(text), do: Regex.scan(~r/\d+/, text)

  @spec is_a_valid_email?(email :: String.t()) :: boolean()
  def is_a_valid_email?(email),
    do: Regex.match?(~r/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/, email)

  @spec is_a_valid_phone_number?(phone_number :: String.t()) :: boolean()
  def is_a_valid_phone_number?(phone_number),
    do:
      Regex.match?(~r/^\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}$/, phone_number)

  @spec is_a_valid_url?(url :: String.t()) :: boolean()
  def is_a_valid_url?(url),
    do: Regex.match?(~r/https?:\/\/[^\s\/$.?#]+\.(?:[a-z]{2,})+(?:\/[^\s$.?#]+)*/, url)
end

ExUnit.start()

defmodule Boterop.RegexTest do
  use ExUnit.Case

  test "get numbers from text" do
    expected_result = "00100505"

    "S0l0 qu1er0 l05 numer05"
    |> Boterop.Regex.get_numbers()
    |> Enum.join()
    |> Kernel.==(expected_result)
    |> assert
  end

  describe "validating email" do
    test "with a valid email" do
      "mail@domain.com"
      |> Boterop.Regex.is_a_valid_email?()
      |> assert
    end

    test "with an invalid tld" do
      "mail@domain.c"
      |> Boterop.Regex.is_a_valid_email?()
      |> refute
    end

    test "with an invalid structure" do
      "mail.domain@com"
      |> Boterop.Regex.is_a_valid_email?()
      |> refute
    end
  end

  describe "validating phone number" do
    test "with a valid country code" do
      "+573015201917"
      |> Boterop.Regex.is_a_valid_phone_number?()
      |> assert
    end

    test "with a valid separator" do
      "301 520 3261"
      |> Boterop.Regex.is_a_valid_phone_number?()
      |> assert
    end

    test "with an invalid number" do
      "911"
      |> Boterop.Regex.is_a_valid_phone_number?()
      |> refute
    end

    test "with an invalid character" do
      "+5730i5203261"
      |> Boterop.Regex.is_a_valid_phone_number?()
      |> refute
    end
  end

  describe "validating url" do
    test "with a valid url" do
      "http://www.boterop.io"
      |> Boterop.Regex.is_a_valid_url?()
      |> assert
    end

    test "without subdomain" do
      "http://boterop.io"
      |> Boterop.Regex.is_a_valid_url?()
      |> assert
    end

    test "with a valid https protocol" do
      "https://www.boterop.io"
      |> Boterop.Regex.is_a_valid_url?()
      |> assert
    end

    test "with an invalid protocol" do
      "invalid://www.boterop.io"
      |> Boterop.Regex.is_a_valid_url?()
      |> refute
    end

    test "with an invalid domain" do
      "https://boterop"
      |> Boterop.Regex.is_a_valid_url?()
      |> refute
    end

    test "with an invalid tdl" do
      "https://boterop.1"
      |> Boterop.Regex.is_a_valid_url?()
      |> refute
    end
  end
end
