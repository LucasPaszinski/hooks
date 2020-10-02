#! /usr/bin/env elixir

defmodule GitHooks.CommitMsg do
  def start do
    [_hook_file, commit_msg_file_path] = System.argv()

    commit_text = File.read!(commit_msg_file_path)

    email = extract_valid_hashtag_value("email")
    release_notes = extract_valid_hashtag_value("release_notes")

    if email == :error or release_notes == :error, do: exit(1)

    if email == false and release_notes == true do
      IO.puts "ERROR: #release_notes with #no_email is invalid, if goes on release notes, must be on email"
      exit(1)
    end

    staged_files = staged_changes()
    current_branch = current_branch()

    if email and not has_required_file_changed("email"), do: exit(1)
    if release_notes, do: has_required_file_changed("release_notes"), do: exit(1)

    exit(0)
  end

  def has_required_files_changes(hashtag_base_name, staged_files, current_branch) do
    if Enum.any?(staged_files, &(&1 == ["M", "next_version_#{hashtag_base_name}_#{current_branch}.md"])) do
      true
    else
      IO.puts "ERROR: The commit message is marked as ##{base_name}, so you must update the file '#{base_file}' with information about your implementation."
      false
    end
  end

  def staged_changes do
    {staged_files, 0} = System.cmd("git", ["diff", "--cached", "--name-status"])

    staged_files
    |> String.split("\n")
    |> Enum.map(&String.split(&1, "\t"))
    |> Enum.filter(&(&1 != [""]))
  end

  def current_branch do
    {current_branch_text, 0} = System.cmd("git", ["rev-parse", "--abbrev-ref", "HEAD", "--"])

    current_branch_text
    |> String.split("\n")
    |> Enum.filter(&(&1 != ""))
  end

  def extract_valid_hashtag_value(commit_msg, hashtag_base_text) do
    tag? = String.contains?(commit_text, "##{hashtag_base_text}")
    no_tag? = String.contains?(commit_text, "#no_#{hashtag_base_text

    case {tag?, no_tag?} do
      {true, true} ->
        IO.puts("ERROR: You can't have both ##{group_tag} and #no_#{group_tag}")
        :errorf

      {false, false} ->
        IO.puts("ERROR: Your commit message need to have one #{group_tag} hashtag like:
      * #no_#{group_tag},
      * #{group_tag}")
        :error

      {_,_} -> tag?
    end
  end
end
