package ru.hackaton.profiler.base

import ru.hackaton.profiler.base.filters.DurationFilter
import ru.hackaton.profiler.base.filters.ExceptionFilter
import ru.hackaton.profiler.base.filters.LibraryFilter
import ru.hackaton.profiler.base.filters.LowSpeedFilter
import ru.hackaton.profiler.base.filters.UrlFilter

object MeasurementFilterService {
    /**
     * List of realized filters
     */
    private val filters = arrayListOf(
        ExceptionFilter(),
        LowSpeedFilter(),
        UrlFilter(),
        LibraryFilter(),
        DurationFilter(),
    )

    fun checkMeasurement(measurement: Measurement) {
        if (filters.any { it.doFilter(measurement) })
            MeasurementApi.sendToServer(measurement)
    }
}