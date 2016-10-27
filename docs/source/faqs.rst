##########################
Frequently Asked Questions
##########################

Why are some properties (e.g. "title" and "description") included in both Dataset and DataDistribution?
--------------------------------------------------------------------------------------------------------
When designing DATS we chose to be flexible and consider some redundancy by including properties in both Dataset as well as DatasetDistribution,
even though in some cases it might be expected that a Dataset property should be inherited by their DatasetDistributions. We followed this approach
to cover cases where repositories may have different information. For example, it would be possible that each DatasetDistribution has more
information in its "description" on how the distribution was produced, adding more details to the general information in the corresponding Dataset.
