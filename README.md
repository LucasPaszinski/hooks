# How to Hook ⚓

## 1. Clone this repository.
## 2. Remember to have python installed and the path environment variable set 🐍
## 3. Run the command below point to this repository path on each of the repositories you want to use this commit rules:
    $ ./repository> git config core.hooksPath "../Hooks" --replace-all
### or if you have git all or pgitall:
    $ gitall . 'git config core.hooksPath "../Hooks" --replace-all'
## 4. Test if is working:
* Make a change on the repository 
* Try to Commit without any tags
* Error should be throw and you should not be able to commit.

## 🎉🎉🎉🎉 Thats It Enjoy !  🎉🎉🎉🎉
