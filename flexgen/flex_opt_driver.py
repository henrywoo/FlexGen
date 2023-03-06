import hiq, argparse, time
from hiq.memory import total_gpu_memory_mb, get_memory_mb
def run_main():
    driver = hiq.HiQLatency(
        hiq_table_or_path=[
            ["flex_opt", "", "run_flexgen", "run_flexgen"],
            ["flex_opt", "OptLM", "init_all_weights", "opt_init_all_weights"],
            ["flex_opt", "OptLM", "generate", "generate"],
            ["flex_opt", "OptLM", "generation_loop_normal", "generation_loop_normal"],
            ["flex_opt", "OptLM", "generation_loop_overlap_single_batch", "generation_loop_overlap_single_batch"],
            ["flex_opt", "OptLM", "generation_loop_overlap_multi_batch", "generation_loop_overlap_multi_batch"],
            # ["flex_opt", "OptLM", "update_attention_mask", "update_attention_mask"],
            # ["flex_opt", "", "init_weight_list", "init_weight_list"],
            # ["flex_opt", "OptLM", "init_weight", "opt_init_weight"],
            # ["flex_opt", "OptLM", "compute_layer", "opt_compute_layer"],
        ],
        metric_funcs= [time.time, total_gpu_memory_mb, get_memory_mb],
        #extra_metrics={hiq.ExtraMetrics.ARGS},
    )
    parser = argparse.ArgumentParser()
    hiq.mod("flex_opt").add_parser_arguments(parser)
    args = parser.parse_args()
    assert len(args.percent) == 6
    hiq.mod("flex_opt").run_flexgen(args)
    driver.show()


if __name__ == "__main__":
    run_main()
