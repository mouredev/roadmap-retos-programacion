defmodule Boterop.Asynchrony do
  @spec timer(seconds :: integer()) :: Task.t()
  def timer(seconds) do
    Task.async(fn ->
      for count <- 1..seconds do
        :timer.sleep(995)
        IO.inspect(count)
      end
    end)
  end

  @spec async_func(name :: String.t(), seconds :: integer()) :: Task.t()
  def async_func(name, seconds) do
    Task.async(fn ->
      print_start(name, seconds)
      :timer.sleep(seconds * 1000)
      print_end(name)
    end)
  end

  @spec a() :: Task.t()
  def a() do
    name = "A"
    seconds = 1

    Task.async(fn ->
      print_start(name, seconds)

      :timer.sleep(seconds * 1000)
      print_end(name)
    end)
  end

  @spec b() :: Task.t()
  def b() do
    name = "B"
    seconds = 2

    Task.async(fn ->
      print_start(name, seconds)

      :timer.sleep(seconds * 1000)
      print_end(name)
    end)
  end

  @spec c() :: Task.t()
  def c() do
    name = "C"
    seconds = 3

    Task.async(fn ->
      print_start(name, seconds)

      :timer.sleep(seconds * 1000)
      print_end(name)
    end)
  end

  @spec d(on_complete_list :: list(Task.t())) :: Task.t()
  def d(on_complete_list) do
    wait_for(on_complete_list)

    Task.async(fn ->
      name = "D"
      seconds = 1

      print_start(name, seconds)

      :timer.sleep(seconds * 1000)
      print_end(name)
    end)
  end

  @spec print_start(name :: String.t(), seconds :: integer()) :: String.t()
  defp print_start(name, seconds), do: IO.inspect("Starting #{name} (#{seconds} sec)")

  @spec print_end(name :: String.t()) :: String.t()
  defp print_end(name), do: IO.inspect("#{name} has finished")

  @spec wait_for(list(Task.t())) :: term()
  defp wait_for([]), do: nil

  defp wait_for([head | tail]) do
    Task.await(head)
    wait_for(tail)
  end
end

timer = Boterop.Asynchrony.timer(15)

Boterop.Asynchrony.async_func("Task 1", 10)
a = Boterop.Asynchrony.a()
b = Boterop.Asynchrony.b()
c = Boterop.Asynchrony.c()
Boterop.Asynchrony.d([a, b, c])

Task.await(timer, 20000)
