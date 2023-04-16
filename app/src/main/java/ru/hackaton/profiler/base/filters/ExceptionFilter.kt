package ru.hackaton.profiler.base.filters

import ru.hackaton.profiler.base.Measurement

class ExceptionFilter : AbstractFilter() {
    override fun doFilter(measurement: Measurement): Boolean {
        super.doFilter(measurement)
        return measurement.status.exception != null
    }
}