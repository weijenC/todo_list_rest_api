#!/bin/bash
# Hardcoded settings
config_file="/opt/config/cognixus_app.ini"
python_path="/usr/bin/python3"
gunicorn_path="/usr/local/bin/gunicorn"

# Dyanmic settins
home_dir=$(sed -nr "/^\[starter\]/ { :l /^home_dir[ ]*=/ { s/[^=]*=[ ]*//; p; q;}; n; b l;}" ${config_file})
ip_server=$(sed -nr "/^\[starter\]/ { :l /^ip_server[ ]*=/ { s/[^=]*=[ ]*//; p; q;}; n; b l;}" ${config_file})
port_server=$(sed -nr "/^\[starter\]/ { :l /^port_server[ ]*=/ { s/[^=]*=[ ]*//; p; q;}; n; b l;}" ${config_file})
workers=$(sed -nr "/^\[starter\]/ { :l /^workers[ ]*=/ { s/[^=]*=[ ]*//; p; q;}; n; b l;}" ${config_file})
thread=$(sed -nr "/^\[starter\]/ { :l /^thread[ ]*=/ { s/[^=]*=[ ]*//; p; q;}; n; b l;}" ${config_file})
timeout=$(sed -nr "/^\[starter\]/ { :l /^timeout[ ]*=/ { s/[^=]*=[ ]*//; p; q;}; n; b l;}" ${config_file})

# Other setting
log_date=$(date +%Y%m%d)
nohup_folder=${home_dir}/nohup
pid_folder=${home_dir}/proc

# Command to check process status
check_process=$(ps aux | grep "${gunicorn_path} server:app --bind ${ip_server}:${port_server}" | grep -v ' grep ' | wc -l)

# Main script
case $1 in
    start)
        echo "Starting To-Do List Web Service..."
        if [ $check_process -eq 0 ];then
            cd ${home_dir}/app/
            nohup ${python_path} ${gunicorn_path} server:app --bind ${ip_server}:${port_server} --workers=${workers} --thread=${thread} --timeout ${timeout} -k uvicorn.workers.UvicornWorker >> ${nohup_folder}/nohup.${log_date} &
            echo $! > ${pid_folder}/pid
        else
            echo "To-Do List Web Service already running"
        fi
    ;;
    stop)
         if [ $check_process -ge 1 ];then
            PID=$(cat ${pid_folder}/pid)
            echo "Stopping To-Do List Web Service..."
            kill $PID
            echo "To-Do List Web Service stopped"
            rm ${pid_folder}/pid
        else
            echo "To-Do List Web Service is not running"
        fi
    ;;
    restart)
        if [ $check_process -ge 1 ];then
            PID=$(cat ${pid_folder}/pid)
            echo "Stopping To-Do List Web Service..."
            kill $PID
            echo "To-Do List Web Service stopped"
            rm ${pid_folder}/pid
        else
            echo "To-Do List Web Service is not running"
        fi
        sleep 10
        echo "Starting To-Do List Web Service..."
        if [ $check_process -eq 0 ];then
            cd ${home_dir}/app/
            nohup ${python_path} ${gunicorn_path} server:app --bind ${ip_server}:${port_server} --workers=${workers} --thread=${thread} --timeout ${timeout} -k uvicorn.workers.UvicornWorker >> ${nohup_folder}/nohup.${log_date} &
            echo $! > ${pid_folder}/pid
        else
            echo "To-Do List Web Service already running"
        fi
    ;;
esac

