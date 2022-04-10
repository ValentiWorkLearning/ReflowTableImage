## Build
```shell
make BR2_EXTERNAL=${REPO_ROOT} -C buildroot O=${REPO_ROOT}/image_build/ orange_table_defconfig
```
## DTS Spi overlay
```dts
&spi1 {
	status = "okay";

        temp-sensor@1 {
            compatible = "maxim,max6675";
            reg = <0>;
            spi-max-frequency = <4300000>;
            spi-cpha;
        };

};
```