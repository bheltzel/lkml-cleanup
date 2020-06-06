dimension: dim_hidden {
    label: "label stuff on the base view"
    hidden: yes
}

dimension: dim_shown {
    label: "label stuff on the base view"
    hidden: yes
}

dimension: dim_not_put_on_extension {
    label: "label stuff on the base view"
    hidden: yes
}

dimension_group: dim_date {
    type: time
    timeframes: [time, hour, date, week, month, year, hour_of_day, day_of_week, month_num, raw, week_of_year,month_name]
    hidden: yes
}