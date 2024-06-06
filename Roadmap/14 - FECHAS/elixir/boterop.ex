defmodule Boterop.Dates do
  @zone_abbr "UTC"
  @utc_offset 3600
  @std_offset 0
  @time_zone "Etc/UTC"

  def get_age(args) do
    current_date = DateTime.now!(@time_zone)
    date = to_date(args)

    current_date
    |> DateTime.diff(date, :day)
    |> Kernel./(360)
    |> trunc()
  end

  def inspect_age(args) do
    args
    |> get_age()
    |> IO.inspect()

    args
  end

  def format(args, format_str) do
    args
    |> to_date()
    |> Calendar.strftime(format_str)
  end

  def inspect_format(args, format_str) do
    args
    |> format(format_str)
    |> IO.inspect()

    args
  end

  defp to_date(args) do
    {day, month, year} = get_keys(args)

    %DateTime{
      day: day,
      month: month,
      year: year,
      hour: 14,
      minute: 30,
      second: 15,
      zone_abbr: @zone_abbr,
      utc_offset: @utc_offset,
      std_offset: @std_offset,
      time_zone: @time_zone
    }
  end

  defp get_keys(args) do
    day = Keyword.get(args, :day, 1)
    month = Keyword.get(args, :month, 1)
    year = Keyword.get(args, :year, 2000)
    {day, month, year}
  end
end

birth_date = [day: 09, month: 10, year: 1999]

birth_date
|> Boterop.Dates.inspect_age()
|> Boterop.Dates.inspect_format("%d/%m/%y")
|> Boterop.Dates.inspect_format("%I:%M:%S %p")
|> Boterop.Dates.inspect_format("%j")
|> Boterop.Dates.inspect_format("%A")
|> Boterop.Dates.inspect_format("%B")
