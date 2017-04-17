for entry in `find /lib/x86_64-linux-gnu -maxdepth 1 -type l -print`
do
  echo "$entry"
  python driver.py "$entry"
done


